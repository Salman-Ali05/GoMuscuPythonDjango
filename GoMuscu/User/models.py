from django.db import models

# Create your models here.

class UserModel(models.Model) :
    userName = models.CharField('User Name', max_length=20, unique=True )
    password = models.CharField('Password', max_length=20, unique=True )
    
    def __str__(self): #self = this
        return self.userName
