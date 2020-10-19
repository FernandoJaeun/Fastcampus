from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register), # register라는 url을 받게 되면 views.py안에 register라는 함수를 호출하라!
]
