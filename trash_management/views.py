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




class TrashBinView(APIView):
    @staticmethod
    def post(request):
        id =request.data.get('id')
        serializer = DustbinPostSerializer(data=request.data)
        print(request.data)
       
        if TrashBin.objects.filter(id=id).exists():    
            trash_bin = TrashBin.objects.get(id=id)
            serializer = DustbinPostSerializer(trash_bin, data=request.data)
        else:
            # If the TrashBin with the given ID doesn't exist, create a new one
            if serializer.is_valid():
                serializer.save()

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(request):
        bins = Dustbin.objects.all()
        serializer = DustbinGetSerializer(instance=bins, many=True)
        