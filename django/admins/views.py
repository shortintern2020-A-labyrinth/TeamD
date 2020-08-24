from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

import json
from django.utils import timezone
import hashlib
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .util.models import post_mail

from company.models import Company


@api_view(['GET', 'POST'])
def accept_company(request):
    if request.method == 'GET':
        try:
            # query_paramが指定されている場合の処理
            token = request.GET.get("token")
            # 更新
            company = Company.objects.get(tokens=token)
            company.is_accepted = 1
            company.save()
            # 企業に申請メール送信
            email = company.email
            subject = "申請承認のおしらせ"
            from_email = "A4sittyo@gmail.com"
            body = "申請が承認されました!\n"
            post_mail(subject, from_email, [email], body)
            return Response(
                {
                    'message': 'update success'
                },
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {
                    'message': 'update error'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    elif request.method == 'POST':
        print()
    elif request.method == 'PUT':
        print()
    elif request.method == 'DELETE':
        print()
