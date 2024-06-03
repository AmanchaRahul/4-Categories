from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    
  user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
  
  
class Goldentries(models.Model):
   date=models.DateField()
   trade_description=models.CharField(max_length=200)
   trade_image=models.ImageField(upload_to="tradeimages")

