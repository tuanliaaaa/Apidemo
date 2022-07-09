
from asyncio.windows_events import NULL
from contextlib import nullcontext
from importlib.metadata import requires

from rest_framework import serializers
from .categoryModel import Category
class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    CategoryName = serializers.CharField(max_length=200)
    CategoryCodeParent = serializers.IntegerField() 
    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.CategoryName = validated_data.get('CategoryName', instance.CategoryName)
        instance.CategoryCodeParent = validated_data.get('CategoryCodeParent', instance.CategoryCodeParent)
        instance.save()
        return instance