from rest_framework import serializers
from apps.book_rest.models import Book

#Serializer de libro este nos permite la conexion entre el modelo y la vista 

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields ='__all__'
        #fields = ['title','author','date_published','editorial','literary_genre']
