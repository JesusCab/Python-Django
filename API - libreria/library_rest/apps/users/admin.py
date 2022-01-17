from django.contrib import admin
from apps.users.models import User

# Registramos nuestro modelo de base de datos de nuestra aplicacion en este archivo

admin.site.register(User)