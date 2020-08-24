from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django import forms

import json
from .models import Question
from .serializers import QuestionSerializer
from movie.models import make_movie
# from youtube.models import upload_movie
from video.models import video_post_validation


# TODO: @コウダイ これパースしてfileとか利用してみて欲しい
def getRequestFormData(req):
    data = {}
    print(req.POST)
    print(req.FILES)

    return data

class BookAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

@api_view(['GET', 'POST'])
def video_view(request):
    if request.method == 'GET':
        return Response({})
    elif request.method == 'POST':
        # multipart/form-dataをパースする
        data = getRequestFormData(request)

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

@api_view(['POST'])
def login(request):
    return Response({"token": "testtokentest"})

@api_view(['POST'])
def logout(request):
    return Response({"message": "success"})

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

        '''
        input = ["material/sample.mp4","material/sample2.mp4","material/sample.mp4"]
        combine_material(input)  #=>output.mp4が作成
        combine_material(input,mmmmm.mp4) #=>mmmmm.mp4が作成
        '''
        # material結合
        combine_material(input)

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
        upload_youtube(file,title,description,category,keywords,privacyStatus)

        # response message
        res = {
            "message": "success!!!",
            "youtube_url": youtube_url
        }

        return Response(res)
    elif request.method == 'DELETE':
        return Response({"message": "Hello, world! from django"})
