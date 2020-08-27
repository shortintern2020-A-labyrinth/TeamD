from django.urls import path

from .views import register_temporary_company, login, logout, video_view, update_company_details, return_preview, return_company_info
from .util.models import post_mail

urlpatterns = [
    path('', return_company_info, name='company_info'),
    path('sendmail', post_mail, name='mail'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('video/', video_view, name='home'),
    path('register/', register_temporary_company),
    path('edit/', update_company_details),
    path('material/preview/', return_preview)
]
