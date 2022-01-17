from ast import Delete
from telnetlib import STATUS
from urllib import request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from apps.book_rest.models import Book
from apps.book_rest.api.serializers import BookSerializer

#definimos la vista para consultar, agregar,u borrar informacion de nuestros libros

class BookAPIView(APIView):
    def get(self,request):
        books =Book.objects.all()
        books_serializer = BookSerializer(books,many = True)
        return Response(books_serializer.data)
    def post(self,request):
        books_serializer =BookSerializer(data=request.data)
        if books_serializer.is_valid():
            books_serializer.save()
            return Response(books_serializer.data, status=status.HTTP_201_CREATED)
        return Response(books_serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

