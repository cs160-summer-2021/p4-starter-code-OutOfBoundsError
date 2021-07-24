# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('memo/', views.memo, name='memo'),
    path('memoboard/', views.memoboard, name='memoboard')
]
