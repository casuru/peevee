# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from rest_framework.reverse import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        user = self.model(
            email=self.normalize_email(email), username=kwargs.get('username')
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)
        
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user
        
class User(AbstractBaseUser, PermissionsMixin):
    
    
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)

    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __unicode__(self):
        
        return self.email

    def get_full_name(self):
        
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        
        return self.first_name
        