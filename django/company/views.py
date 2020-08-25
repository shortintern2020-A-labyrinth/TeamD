from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django import forms

import json
import random
import string
import time
from .models import Company
from video.models import video_post_validation, material_video_validation, save_video, remove_video, get_video_post
from .util.models import post_mail
from django.utils import timezone
import hashlib
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from session.redis import SessionRedis

@csrf_exempt
@api_view(['GET', 'POST'])
def video_view(request):
    if request.method == 'GET':
        company_id = int(request.GET.get('company_id'))

        # [{'name':'hoge', 'youtube_url':'hoge.com', ・・・},・・・]
        videos = get_video_post(company_id)
        return Response(
            {
                'message': 'success!',
                'videos': videos
            },
            status=status.HTTP_200_OK
        )
    elif request.method == 'POST':
        if not video_post_validation(request.POST):
            return Response(
                {
                    'message': 'video_post_validation error'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        if not material_video_validation(request.FILES):
            return Response(
                {
                    'message': 'material_video_validation error'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        # data['title']='タイトル', data['description']='概要'・・・
        data = json.loads(json.dumps(request.POST))
        # file_infos = [{'name':'ファイル名', 'path':'/tmp/ファイル名'}, ・・・]
        file_infos = [save_video(video)
                      for video in request.FILES.getlist('movies')]
        data['file_infos'] = file_infos
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
    if request.method == 'GET':
        return Response({})
    elif request.method == 'POST':
        data = json.loads(request.body)
        name = data['name']
        email = data['email']
        password = data['password']
        description = data['description']
        is_accepted = 0  # 仮登録

        # 会員登録用トークン生成（メールアドレス + パスワード + システム日付のハッシュ値とする）
        date = timezone.now()
        tmp_str = email + password + date.strftime('%Y%m%d%H%M%S%f')
        token = hashlib.sha1(tmp_str.encode('utf-8')).hexdigest()
        # compnayテーブルにインサート
        company = Company(name=name, email=email, password=password,
                          description=description, is_accepted=is_accepted, tokens=token)
        company.save()
        # 運営に申請メール送信
        subject = "企業からの申請依頼のお知らせ"
        to_email = "A4sittyo@gmail.com"
        body = "企業名: " + name + "\n メールアドレス:" + email + "\n 企業概要: " + \
            description + "\n　申請する rakutenpv.app/api/admin/accept/company?token=" + token
        post_mail(subject, email, [to_email], body)

        return JsonResponse(
            {
                'message': 'success'
            },
            status=status.HTTP_200_OK
        )
    elif request.method == 'PUT':
        print()
    elif request.method == 'DELETE':
        print()
