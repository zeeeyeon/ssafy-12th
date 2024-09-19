# 명시적 상대 경로(현재 위치에서 views를 import 하겠다.)
from . import views
from django.urls import path, include

urlpatterns = [
    path('index/', views.index, name='index'),
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.greeting, name='greeting'),
]