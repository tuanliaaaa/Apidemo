from dataclasses import field
from pyexpat import model
from unicodedata import category
from rest_framework import serializers
from .models import User,Post,Category
class Useripa(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class Categoryipa(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class Articlessipa(serializers.ModelSerializer):
    User = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),
                                                many=False)     
    Category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),
                                                  many=False)  
    class Meta:
        model = Post
        fields = '__all__'
    