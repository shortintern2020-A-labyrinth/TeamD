from django.urls import path

from .views import register_temporary_company, accept_temporary_company
from .util.models import post_mail

urlpatterns = [
    path('sendmail', post_mail, name='mail'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('video/', video_view, name='home'),
    path('register', register_temporary_company),
    path('accept/company', accept_temporary_company),
]
