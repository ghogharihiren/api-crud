from django.contrib.auth.models import User
from rest_framework import serializers
from .models import*



class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['username', 'email']

class ArticalSerializers(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields="__all__"
        
        
    