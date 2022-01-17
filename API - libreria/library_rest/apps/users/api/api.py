from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

#definimos la vista para consultar, agregar,u borrar informacion de nuestros usuarios

class UserAPIView(APIView):
    def get(self,request):
        users =User.objects.all()
        users_serializer = UserSerializer(users,many = True)
        return Response(users_serializer.data)
    def post(self,request):
        serializer =UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  