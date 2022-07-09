import errno
from re import T
from wsgiref import validate
from django.forms import ValidationError
from pkg_resources import require
from rest_framework import serializers

from .articlesModel import Articles
from .userModel import User
from .articlesSerializer import ArticlesSerializer
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False) 
    UserName = serializers.CharField(max_length=200)
    Age = serializers.IntegerField(required=False)
    Email = serializers.EmailField()
    Password = serializers.CharField()
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop('Password',None)
        return ret
    def validate(self, data):
        error=False
        try:
            user = User.objects.get(UserName=data['UserName']) 
            error=True
        except:
            error= False
        finally:
            if(error):
                raise serializers.ValidationError("User đã tồn tại")
        return data
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.UserName = validated_data.get('UserName', instance.UserName)
        instance.Age = validated_data.get('Age', instance.Age)
        instance.Email = validated_data.get('Email', instance.Email)
        instance.Password = validated_data.get('Password', instance.Password)
        instance.save()
        return instance