from rest_framework import serializers
from authentication import models


class CreateUserSerializer(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(write_only = True, required = False)
    
    
    def validate(self, data):
        
        if data['confirm_password'] != data['password']:
            
            raise serializers.ValidationError("Passwords must match")
            
        return data
    
    def create(self, validated_data):
        
        return models.User.objects.create_user(**validated_data)
        
    class Meta:
        
        fields = "__all__"
        model = models.User
        

        
class UserSerializer(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(write_only = True, required = False)
        
    
    def update(self, instance, validated_data):
        
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.save()
        
        password, confirm_password = validated_data.get("password", None), validated_data.get("confirm_password", None)
        
        if password is not None and confirm_password == password:
            
            instance.set_password(password)
        
        return instance
        
        
    class Meta:
            
        fields = "__all__"
        extra_kwargs = {
            "password":{
                "write_only":True,
                "required":False
            }
        }
            
        model = models.User
        
        

class PasswordSerializer(serializers.Serializer):
    
    def validate(self, data):
        
        if data["password"] != data['confirm_password']:
            
            raise serializers.ValidationError("Both passwords must match.")
        
        return data
    
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    