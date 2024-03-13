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
    
    
    
    
class UserLogin(APIView):
    permission_classes = [AllowAny]
    @staticmethod
    def post(request):
        data = request.data
        email = data.get('email')
        password =data.get('password')
        user = authenticate(email=email,passwword=password)
        
        if user is not None:
            login(request,user)
            user_id = User.objects.get('email')
            user_info = UserSerializer(instance=user_id,many=false).data
            token,created = Token.objects.get_or_create(user=user)
            response ={
                'login':True,
                'token':token.key,
                'user':user_info
            }
            return Response(message)
        else:
            response ={
                'login':false,
                'msg':'Invalid username or password'
            }        
            
            return Response(response)

# {
#     "email":"admin@gmail.com",
#     "password":"admin"
# }


class ZoneView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serializer = ZoneSerializer(data=data);
        if serializer.is_valid():
            serializer.save()
            return Response({'save':True})
        return Response({'save':False,
                         'msg': serializer.errors
                         })
        
    @staticmethod
    def get(request):
        try:
            zones = Zone.objects.all()  # Retrieve all zones
            serializer = ZoneSerializer(zones, many=True)  # Serializing the fetched zones
            return Response(serializer.data)  # this returns serialized data as a JSON response
        except Exception as e:
            return Response({'error': str(e)}, status=500)  # Handling  errors
        
