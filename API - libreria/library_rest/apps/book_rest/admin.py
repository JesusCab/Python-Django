from django.contrib import admin
from apps.book_rest.models import Book

# Registramos nuestro modelo de base de datos de nuestra aplicacion en este archivo

admin.site.register(Book)
