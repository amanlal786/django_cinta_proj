from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=255, min_length=2)
    age=serializers.IntegerField(max_value=150,min_value=2)
    skills=serializers.CharField()
    # class Meta:
    #     model=User
    #     fields=['name', 'age', 'skills',]

    # def validate(self,attrs):
    #     #check image similarity
    #     return super().validate(attrs)
    
    # def create(self,validated_data):
    #     return User.objects.create_user(validated_data)