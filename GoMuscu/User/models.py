from django.db import models

# Create your models here.

class UserModel(models.Model):
    userName = models.CharField('User Name', max_length=20, unique=True)
    password = models.CharField('Password', max_length=20)
    refresh_token = models.CharField('Refresh Token', max_length=255, null=True, blank=True)
    access_token = models.CharField('Access Token', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.userName
