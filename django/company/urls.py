from django.urls import path

from .views import register_temporary_company
from .util.models import post_mail

urlpatterns = [
    path('sendmail', post_mail, name='mail'),
    path('register', register_temporary_company),
]
