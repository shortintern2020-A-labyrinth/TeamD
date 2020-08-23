from django.core.mail import send_mail
from django.http import HttpResponse

# Create your models here.

def sendMail(subject="題名", from_email="A4sittyo@gmail.com", to_email=["naoki@mail.com"], body="本文"): #一応テスト用に引数デフォルトで設定

    send_mail(subject, body, from_email, to_email)
    return HttpResponse('<h1>email send complete.</h1>')
