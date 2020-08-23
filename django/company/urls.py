from django.urls import path

from .views import BookAPIView, VideoView
from .util.models import sendMail

urlpatterns = [
    path('', BookAPIView.as_view(), name='home'),
    path('video/', VideoView, name='home'),
    path('sendmail', sendMail, name='mail')
]
