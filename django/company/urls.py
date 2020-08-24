from django.urls import path

from .views import BookAPIView, VideoView, video_view
from .util.models import post_mail

urlpatterns = [
    path('', BookAPIView.as_view(), name='home'),
    path('video/', video_view, name='home'),
    path('sendmail', post_mail, name='mail')
]
