from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django import forms

import json
from .models import Company
from .serializers import CompanySerializer
from video.models import video_post_validation
from .util.models import post_mail
from django.utils import timezone
import hashlib
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# TODO: @コウダイ これパースしてfileとか利用してみて欲しい
def getRequestFormData(req):
    data = {}
    print(req.POST)
    print(req.FILES)

    return data

class BookAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class CompanyAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

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

# 企業の仮登録


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
            description + "\n　申請する rakutenpv.app/api//accept/company/?token=" + token
        post_mail(subject, email, [to_email], body)

        return JsonResponse(
            {
                'message': 'ok'
            },
            status=status.HTTP_200_OK
        )
    elif request.method == 'PUT':
        print()
    elif request.method == 'DELETE':
        print()

    # 運営に申請メール送信
    # subject="企業からの申請依頼のお知らせ"
    # to_email="A4sittyo@gmail.com"
    # body="企業名: " + company_name + "\n メールアドレス:" + email + "\n 企業概要: " + description + "\n　申請する rakutenpv.app/api//accept/company/?token=" + token
    # post_mail(subject, email, to_email, body)
