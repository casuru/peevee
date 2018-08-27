# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from authentication import serializers, models

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    
    def get_serializer_class(self):
        
        if self.request.method == "POST":
            
            return serializers.CreateUserSerializer
        
        return serializers.UserSerializer
        
    
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
