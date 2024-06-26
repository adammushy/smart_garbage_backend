from django.db import  models
from django.contrib.auth.models import AbstractUser
import uuid
from user_management.models import *

# create your models here
        
class Dustbin(models.Model):
    id =models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    # zone = models.ForeignKey(Zone,on_delete=models.CASCADE)
    lat = models.FloatField()
    lon= models.FloatField()
    percentage =models.CharField(max_length=5)
    status =models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'dustbin'
#  {
#      "id":"1234qwerty",
#      "name":"mbezi beach",
#      "lat":-6.7335522,
#      "lon":39.2108993,
#      "percentage":76,
#      "status":"almost full"
#  }       
class Report(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    driver=models.ForeignKey(User, on_delete=models.CASCADE)
    description =models.TextField()
    attachment = models.TextField()#this will be binary data
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table ='report'
    

class Complain(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    reportername = models.CharField(max_length=100, null=False,blank=False)
    reporterphone = models.CharField(unique=False,max_length=20)
    reporteremail=models.EmailField(null=False)
    attachment = models.TextField()# for the use of image in binary
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
        
    class Meta:
        db_table = 'complain'
        

        
        