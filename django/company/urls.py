from django.urls import path

from .views import BookAPIView, VideoView

urlpatterns = [
    path('', BookAPIView.as_view(), name='home'),
    path('video/', VideoView, name='home'),
]
