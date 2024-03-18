from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =[
            'id',
            'username',
            'email',
            'phone',
            'usertype',
            'password'   
        ]
        
        extra_kwargs = {"password":{"write_only":True}}
        
    def create(self,validate_data):
        user =User.objects.create_user(**validate_data)
        return user
    
    
class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields ='__all__'
        


    
        