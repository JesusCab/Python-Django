from unicodedata import name
from django.urls import path
from apps.book_rest.api.api import BookAPIView 

urlspatterns=[
    path('libro/',BookAPIView.as_view(),name='libro_api'),
]