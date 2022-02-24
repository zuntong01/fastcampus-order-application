from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_type = models.IntegerField()  #0: 일반사용자, 1: 사장님, 2: 배달기사

