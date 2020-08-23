from django.urls import path

from .views import BookAPIView, VideoView, video_view

urlpatterns = [
    path('', BookAPIView.as_view(), name='home'),
    path('video/', video_view, name='home'),
]
