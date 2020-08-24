from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

import json
from .models import Question, Company
from .serializers import QuestionSerializer
from movie.models import make_movie
from youtube.models import upload_movie
from video.models import video_post_validation
from .util.models import post_mail
from django.utils import timezone
import hashlib


class BookAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


@api_view(['GET', 'POST'])
def video_view(request):
    if request.method == 'GET':
        return Response({})
    elif request.method == 'POST':
        data = json.loads(request.body)
        if not video_post_validation(data):
            return Response(
                {
                    'message': 'error'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

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

# バリデーション
def VideoPostValidation(data):
    return True

#企業の仮登録
def register_temporary_company(request):
    company_name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    description = request.POST['description']
    is_accepted = 0 #仮登録

     # 会員登録用トークン生成（メールアドレス + パスワード + システム日付のハッシュ値とする）
    date = timezone.now()
    tmp_str = email + password + date.strftime('%Y%m%d%H%M%S%f')
    token = hashlib.sha1(str.encode('utf-8')).hexdigest()    # utf-8でエンコードしないとエラーになるらしい

    #compnayテーブルにインサート
    company = Company(name=company_name, email=email, password=password, description=description, is_accepted=is_accepted, token=token)
    company.save()

    #運営に申請メール送信
    subject="企業からの申請依頼のお知らせ"
    to_email="A4sittyo@gmail.com"
    body="企業名: " + company_name + "\n メールアドレス:" + email + "\n 企業概要: " + description + "\n　申請する rakutenpv.app/api//accept/company/?token=" + token
    post_mail(subject, email, to_email, body)

#仮登録企業の承認
def accept_temporary_company(request):
    if "token" in request.GET:
        # query_paramが指定されている場合の処理
        param_value = request.GET.get("token")
        #更新
        uniq_company = Company.objects.get(token=param_value)
        uniq_company.is_accepted = 1
        b.save() #UPDATE
    else:
        # query_paramが指定されていない場合の処理
        return Response(
            {
                "message": "something wrong happened",
            },
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET', 'POST'])
def VideoView(request):
    if request.method == 'GET':
        return Response({"message": "Hello, world! from django"})
    elif request.method == 'POST':
        # request body取得
        data = json.loads(request.body)

        # バリデーション
        if not VideoPostValidation(data):
            return Response(
                {
                    "message": "validation error, please check it",
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # video整形
        video = make_movie(data)

        # youtubeにアップロード
        '''
        入力例
        file = 'movie/sample.mp4'
        title = "Video title"
        description = "test description"
        category = "22"
        keywords = "tag"
        privacyStatus = "public"
        '''
        youtube_url = upload_youtube(file,title,description,category,keywords,privacyStatus)

        # response message
        res = {
            "message": "success!!!",
            "youtube_url": youtube_url
        }

        return Response(res)
    elif request.method == 'DELETE':
        return Response({"message": "Hello, world! from django"})
