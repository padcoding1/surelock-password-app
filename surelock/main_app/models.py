from django.db import models

# Create your models here.

class Login(models.Model):
    appname = models.CharField(max_length=100)
    username =  models.CharField(max_length=100)
    password =  models.CharField(max_length=100)
    note = models.TextField(max_length=250)

    def __str__(self):
        return self.appname    
