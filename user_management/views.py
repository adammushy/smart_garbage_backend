from django.shortcuts import render

# Create your views here.
from .models import *
from .serializer import * 
from rest_framework.views import APIView
from  rest_framework.response import Response
from django.db.models import QuerySet
from rest_framework.generics import UpdateAPIView
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated


class RegisterUser(APIView):
    permission_classes =[AllowAny]
    @staticmethod
    def post(request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            email = data['email']
            user = User.objects.filter(email=email)
            if user:
                message = {'status': False, 'message': 'username or email already exists'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
            userr = serializer.save()
        message = {'save':false,'errors':serializer.errors}
        return Response(message)


    @staticmethod
    def get(request):
        users=User.objects.all()
        return Response(UserSerializer(instance=user,many=True).data)            
    
    #how data is returned JSON
    # {
    #     'name':"John Doe",
    #     'email':"john@gmail.com",
    #     'phone':9876543210,
    #     'usertype':"admin",
    #     'password':"password"
    # }
    
    
    
    