from django.urls import path

from .views import category_view

urlpatterns = [
    path('categories/', category_view, name='category_list'),
]
