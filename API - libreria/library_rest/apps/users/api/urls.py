from unicodedata import name
from django.urls import path
from apps.users.api.api import UserAPIView 

urlspatterns=[
    path('usuario/',UserAPIView.as_view(),name='usuario_api'),
]