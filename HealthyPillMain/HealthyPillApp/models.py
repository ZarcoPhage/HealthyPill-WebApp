from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    ''''Manager para perfiles de usuarios'''

    def create_user(self, username, email, password=None):
        ''''Crear nuevo userprofile'''
        #user = self.create_user(username, email, name, password)
        if not email:
            raise ValueError('Debe ingresar un correo')
        

        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    


class UserProfile(AbstractBaseUser, PermissionsMixin):
    ''''Modelo Base de datos para usuarios en el sistema'''
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    #name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_pacient = models.BooleanField(default=False)
    is_specialist = models.BooleanField(default=False)


    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_username(self):
        ''''Retorna cadena representando al usuario'''
        return self.username
   
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()