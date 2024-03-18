

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
from django.contrib.auth import authenticate,login,update_session_auth_hash


class RegisterUser(APIView):
    permission_classes = [AllowAny]
    @staticmethod
    def post(request):
        data = request.data
        print(data)
        serializer = UserSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            print("DDDDD")
            email = data['email']
        
            user = User.objects.filter(email=email)
            if user:
                message = {'status': False, 'message': 'username or email already exists'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
            userr = serializer.save()
            message = {'save': True}
            return Response(message)
        message = {'save':False,'errors':serializer.errors}
        return Response(message)


    @staticmethod
    def get(request):
        users=User.objects.all()
        return Response(UserSerializer(instance=user,many=True).data)            
    
    #how data is returned JSON
    # {
    #     "name":"John Doe",
    #     "email":"john@gmail.com",
    #     "phone":9876543210,
    #     "usertype":"admin",
    #     "password":"password"
    # }
    
    
    
class UserLogin(APIView):
    permission_classes = [AllowAny]
    @staticmethod
    def post(request):
         
        email = request.data.get('email')
        password =request.data.get('password')
        # print(email + password)
        
        user = authenticate(email=email,password=password)
        # print(user)
        if user is not None:
            login(request,user)
            print("ddddd")
            user_id = User.objects.get(email=email)
            print(user_id)
            user_info = UserSerializer(instance=user_id,many=False).data
            # token, created = Token.get_or_create(user=user)
            token, created  = Token.objects.get_or_create(user=user)
            response ={
                'login':True,
                'token':token.key,
                'user':user_info
            }
            return Response(response)
        else:
            response ={
                'login':False,
                'msg':'invalid username or password'
                # 'msg':user_info.errors
            }        
            
            return Response(response)

# {
#     "email":"admin@gmail.com",
#     "password":"admin"
# }

# {
#     "email":"john@gmail.com",
#     "password":"123456"
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
        


# {
#     "email":"admin@gmail.com",
#     "password":"admin"
# }

# {
#     "email":"john@gmail.com",
#     "password":"123456"
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
        
