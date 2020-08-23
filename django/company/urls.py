from django.urls import path

from .views import BookAPIView, VideoView
from .util.models import post_mail

urlpatterns = [
    path('', BookAPIView.as_view(), name='home'),
    path('video/', VideoView, name='home'),
    path('sendmail', post_mail, name='mail')
]
