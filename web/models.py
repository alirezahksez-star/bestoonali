from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class expence (models.Model):
    text = models.TextField(max_length=255)
    date = models.DateField()
    amount = models.BigIntegerField()
    
    user = models.ForeignKey(User , on_delete=models.CASCADE)

class incom (models.Model):
    text = models.TextField(max_length=255)
    date = models.DateField()
    amount = models.BigIntegerField()
    
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    