"""library_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
#importamos nuestras vistas de apps
from apps.users.api.api import UserAPIView 
from apps.book_rest.api.api import BookAPIView 

#configuracion de las rutas/urls con path
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('usuario/', include('apps.users.api.urls')), 
    path('usuario/',UserAPIView.as_view(),name='usuario_api'),
    path('libro/',BookAPIView.as_view(),name='libro_api'),
]
