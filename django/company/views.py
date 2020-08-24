from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

import json
from .models import Question, Company
from .serializers import QuestionSerializer
from movie.models import make_movie
from youtube.models import upload_movie
from video.models import video_post_validation
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

#企業の仮登路
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
    company = Blog(name=company_name, email=email, password=password, description=description, is_accepted=is_accepted, token=token)
    company.save()



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
