from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django import forms

import json, base64, io, os
import random
import string
import time
from .models import Company, Urls
from video.models import video_post_validation, material_video_validation, save_video, remove_video, get_video_post, get_request_data, set_video_post
from .util.models import post_mail
from django.utils import timezone
import hashlib
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from session.redis import SessionRedis
from company.util.models import get_company_id
from movie.models import making_movie
from youtube.models import upload_movie

@api_view(['GET'])
def return_company_info(request):
    try:
        sessionRedis = SessionRedis()
        token = request.headers['Authorization']
        str_time, company_id = sessionRedis.get(token)
        company = Company.objects.get(id=company_id)
        return Response(
                {
                    'name': company.name,
                    'description': company.description
                },
                status=status.HTTP_200_OK
            )
    except:
        return Response(
                {
                    'message': 'failed!'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

@csrf_exempt
@api_view(['GET', 'POST'])
def video_view(request):
    if request.method == 'GET':
        token = request.headers['Authorization']
        _, company_id = get_company_id(token)
        company_id = None if company_id == None else int(company_id)
        if company_id != None:
            videos = get_video_post(company_id) # [{'name':'hoge', 'youtube_url':'hoge.com', ・・・},・・・]
            return Response(
                {
                    'message': 'success!',
                    'videos': videos
                },
                status=status.HTTP_200_OK
            )
    elif request.method == 'POST':
        # 動画公開時の情報に対してバリデーション
        if not video_post_validation(request.POST):
            return Response(
                {
                    'message': 'video_post_validation error'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        # 素材動画に対してバリデーション
        if not material_video_validation(request.FILES):
            return Response(
                {
                    'message': 'material_video_validation error'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        data = get_request_data(request)  # リクエストパラメータの取得

        data = making_movie(data) #動画加工

        #data = upload_movie(data) #動画アップロード

        # 仮保存した動画を削除する
        # for file_path in data['delete']:
        #     remove_video(file_path)
        set_video_post(data) # 公開した動画のURLをデータベースにいれる
        return Response(
            {
                'message': 'success'
            },
            status=status.HTTP_200_OK
        )
    elif request.method == 'PUT':
        print()
    elif request.method == 'DELETE':
        print()

@api_view(['POST'])
def return_preview(request):
    try:
        # バリデーション
        if not material_video_validation(request.FILES):
            return Response(
                {
                    'message': 'material_video_validation error'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        data = get_request_data(request)

        #動画加工
        data = making_movie(data)

        # 仮保存した動画を削除する
        # remove_video(data['delete'])

        #編集後の動画返却
        path = data['edit']['combine']['paths']
        file_path = path[0]

        paths = file_path.split('/')
        paths[1] = "after-" + paths[1]
        after_file = '/'.join(paths)

        s = "ffmpeg -i {} -vcodec libx264 {}".format(file_path, after_file)

        # コーデックをh264に設定した
        os.system(s)

        video = io.open(after_file, 'r+b').read()
        encoded_video = base64.b64encode(video)

        return HttpResponse(encoded_video.decode('ascii'), content_type='video/mp4')
    except:
        return Response(
            {
                'message': 'failed'
            },
            status=status.HTTP_400_BAD_REQUEST
        )


# session用
def randomSTR(n):
    randlst = [random.choice(string.ascii_letters + string.digits)
               for i in range(n)]
    return ''.join(randlst)


@csrf_exempt
@api_view(['POST'])
def login(request):
    try:
        # emailとpasswordの一致確認
        data = json.loads(request.body)
        email = data['email']
        password = data['password']
        company = Company.objects.get(email=email)
        is_accepted = company.is_accepted
        if password == company.password and is_accepted == 1:

            # random でsession作成
            session = randomSTR(10)
            current_time = time.time()

            # session key: session, value: current_time
            sessionRedis = SessionRedis()
            sessionRedis.setToken(session, current_time, company.id)

            return Response({'token': session})
        else:
            raise Exception
    except:
        return Response(
            {
                'message': 'input data is not correct or not accepted yet'
            },
            status=status.HTTP_400_BAD_REQUEST
        )


@csrf_exempt
@api_view(['POST'])
def logout(request):
    token = request.headers['Authorization']
    sessionRedis = SessionRedis()
    sessionRedis.delete(token)
    return Response(
        {
            'message': 'logged out successfully.'
        },
        status=status.HTTP_200_OK
    )


@csrf_exempt
def register_temporary_company(request):
    try:
        if request.method == 'GET':
            return Response({})
        elif request.method == 'POST':
            data = json.loads(request.body)
            name = data['name']
            email = data['email']
            password = data['password']
            description = data['description']

            # 会員登録用トークン生成（メールアドレス + パスワード + システム日付のハッシュ値とする）
            date = timezone.now()
            tmp_str = email + password + date.strftime('%Y%m%d%H%M%S%f')
            token = hashlib.sha1(tmp_str.encode('utf-8')).hexdigest()
            # compnayテーブルにインサート
            company = Company(name=name, email=email, password=password,
                                description=description, is_accepted=0, tokens=token)
            company.save()

            # urlsの登録
            urls = data['urls']
            for url in urls:
                value = url['value']
                type = url['type']
                if value == '':
                    continue
                urls = Urls(value=value, type=type, company_id=company.id)
                urls.save()

            # 運営に申請メール送信
            subject = "企業からの申請依頼のお知らせ"
            to_email = "A4sittyo@gmail.com"
            body = "企業名: " + name + "\n メールアドレス:" + email + "\n 企業概要: " + \
                description + "\n　申請する rakutenpv.app/api/admin/accept/company?token=" + token
            post_mail(subject, email, [to_email], body)

            return JsonResponse(
                {
                    'message': 'registerd successfully!'
                },
                status=status.HTTP_200_OK
            )
        elif request.method == 'PUT':
            print()
        elif request.method == 'DELETE':
            print()
    except:
        return JsonResponse(
            {
                'message': 'register failed!'
            },
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['PUT'])
def update_company_details(request):
    try:
      data = json.loads(request.body)
      token = request.headers['Authorization']
      _, company_id = get_company_id(token)
      company_id = None if company_id == None else int(company_id)
      description = data['description']
      company = Company.objects.get(id=company_id)
      company.description = description
      company.save()
      # urlsの登録
      urls = data['urls']
      if urls:
          for url in urls:
              value = url['value']
              if value == '':
                continue
              type = url['type']
              try:
                  urls = Urls.objects.get(type=type, company_id=company.id)
                  urls.value = value
              except Urls.DoesNotExist:
                  urls = Urls(value=value, type=type, company_id=company.id)
              urls.save()
      return JsonResponse(
          {
              'message': 'success'
          },
          status=status.HTTP_200_OK
      )
    except:
        return Response(
            {
                'message': 'failed'
            },
            status=status.HTTP_400_BAD_REQUEST
        )


    # 運営に申請メール送信
    # subject="企業からの申請依頼のお知らせ"
    # to_email="A4sittyo@gmail.com"
    # body="企業名: " + company_name + "\n メールアドレス:" + email + "\n 企業概要: " + description + "\n　申請する rakutenpv.app/api//accept/company/?token=" + token
    # post_mail(subject, email, to_email, body)
