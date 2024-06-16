from django.shortcuts import render
from .models import *
from .serializer import * 
from rest_framework.views import APIView
from  rest_framework.response import Response
from django.db.models import QuerySet
from rest_framework.generics import UpdateAPIView
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import *
from rest_framework.authentication import *
from rest_framework.apps import *
import random


class TrashBinView(APIView):
    @staticmethod
    def post(request):
        id =request.data.get('id')
        serializer = DustbinPostSerializer(data=request.data)
        print(request.data)
       
        if Dustbin.objects.filter(id=id).exists():    
            trash_bin = Dustbin.objects.get(id=id)
            serializer = DustbinPostSerializer(trash_bin, data=request.data)
        else:
            # If the TrashBin with the given ID doesn't exist, create a new one
            if serializer.is_valid():
                serializer.save()

        if serializer.is_valid():
            return Response({"data":serializer.data,"msg": "data saved"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        bins = Dustbin.objects.all()
        serializer = DustbinGetSerializer(instance=bins, many=True)
        return Response(serializer.data)


class ReportView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serializer= ReportPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "save": True,
                "msg": "Report sumbitted successfully"
            })
        return Response({
            "save":False,
            "msg": serializer.errors
        })
        
# {
#     "driver":"hemed",
#     "description": "weqewqewqeqw",
#     "attachment":"image",
#     } 

    @staticmethod
    def get(request):
        id = request.GET.get('id')
        print(f"ID: {id}")
        q = request.GET.get('q')
        if q=="s":
            try:
                reports = Report.objects.filter(driver=id)
                print(f"reports from driver: {reports}")
                serializer = ReportGetSerializer(instance=reports, many=True)
                response = {"status": True, "data": serializer.data}
                
                return Response(response)
            except Report.DoesNotExist:
                return Response({"status": False, "msg": "No report found"})
            
        elif q=="a":
            reports = Report.get.all()
            serializer = ReportGetSerializer(instance=posts, many= True)
            if serializer is not None:
                return Response({"status":True, "data":serializer.data})
            return Response(serializer.errors)
        

class ComplainView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serializer = ComplainPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response ={
                'success': True,
                'msg': 'Successfully submitted'
            }
            print(response)
            return Response()
        return Response({
            'success':False,
            'msg': serializer.errors
        })          
        
    
# {
#     "reportername":"Mastra codes",
#     "reporterphone":"2555799900000",
#     "reportemail":"adam@gmail.com",
#     "attachment":"image",
#     "description":"this and that",
# }
    @staticmethod
    def get(request):               
        complains = Complain.objects.all()
        serializer=ComplainsGetSerializer(compains,many=True)
        return Response(serializer.data)
    
