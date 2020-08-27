from django.core.mail import send_mail
from django.http import HttpResponse
from session.redis import SessionRedis

# Create your models here.


# 一応テスト用に引数デフォルトで設定
def post_mail(subject="題名", from_email="A4sittyo@gmail.com", to_email=["naoki@mail.com"], body="本文"):

    send_mail(subject, body, from_email, to_email)
    return HttpResponse('<h1>email send complete.</h1>')


def get_company_id(token):
    # sessionからvalueを取得
    sessionRedis = SessionRedis()
    str_time, company_id = sessionRedis.get(token)
    return str_time, company_id
