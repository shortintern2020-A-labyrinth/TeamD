from django.urls import path

from .views import BookAPIView, VideoView, register_temporary_company
from .util.models import post_mail

urlpatterns = [
    path('', BookAPIView.as_view(), name='home'),
    path('video/', VideoView, name='home'),
    path('sendmail', post_mail, name='mail'),
    path('company/register', register_temporary_company),
]
