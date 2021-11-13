from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    ''''Manager para perfiles de usuarios'''

    def create_user(self, username, email, password=None):
        ''''Crear nuevo userprofile'''
        user = self.create_user(username, email, password)
        if not email:
            raise ValueError('Debe ingresar un correo')
        

        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password, email=None):
        user = self.create_user(username, password, email)
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
    #REQUIRED_FIELDS = ['name', 'email']
    
    def __str__(self):
        ''''Retorna cadena representando al usuario'''
        return self.username

    def __str__(self):
        ''''Retorna cadena representando al usuario'''
        return self.email

    #def get_full_name(self):
    #    ''''Retorna nombre completo'''
    #    return self.name
    
    #def get_short_name(self):
    #    ''''Retorna nombre corto'''
    #    return self.name



