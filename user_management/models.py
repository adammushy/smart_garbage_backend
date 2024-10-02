
from django.db import  models
from django.contrib.auth.models import AbstractUser
import uuid






class Zone(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    name=models.CharField(max_length=50)
    city =models.CharField(max_length=50)
    district =models.CharField(max_length=100)        
    ward = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'zone'
class User(AbstractUser):
    
    TYPES =(
        ("ADMIN","user is super admin"),
        ("AGENT","user is admin of company"),
        ("DRIVER","truck driver"),
    )
    
    
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone=models.CharField(max_length=15,unique=True)
    zone = models.ForeignKey(Zone,on_delete=models.CASCADE, null=True)
    usertype=models.CharField(choices=TYPES,max_length=20)
    
    USERNAME_FIELD="email"
    REQUIRED_FIELDS =[]
    
    def __str__(self):
        return self.username
    
    
    class Meta:
        db_table = 'user'
                
        

    