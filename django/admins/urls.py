from django.urls import path

from .views import accept_company

urlpatterns = [
    path('accept/company/', accept_company, name='accept_company'),
]
