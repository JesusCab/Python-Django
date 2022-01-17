from rest_framework import serializers
from apps.users.models import User

#Serializer de Usuario este nos permite la conexion entre el modelo y la vista 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'
        #fields = ['id','password','last_login','username','name','last_name','email','image','is_active','is_staff','is_superuser']
