from rest_framework import serializers
from .models import *


class DustbinPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dustbin
        fields ='__all__'


class DustbinGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dustbin
        fields = '__all__'        
        depth = 1
        
class ReportPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields =[
            'driver',
            'attachment',
            'description',
            ]
        
class ReportGetSerializer(serializers.ModelSerializer):
    class Meta:
        model =Report
        fields='__all__'
    def to_representation(self, instance):
        response= super().to_representation(instance)
        driver = instance.driver
        response ["driver"] ={
            "id":driver.id,
            "name": driver.username,
            "phone":driver.phone,
            "email":driver.email
        }
        
        return response
 
class ComplainPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields =[
            'reportername',
            'reporterphone',
            'reporteremail',
            'attachment',
            'description'
        ]
        
class ComplainGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = '__all__'
        depth =1
        