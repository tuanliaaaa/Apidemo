from this import s
from pkg_resources import require
from rest_framework import serializers
from .articlesModel import Articles
from .userModel import User
from .categoryModel import Category
# from .userSerializer import UserSerializer
from .categorySerializer import CategorySerializer
class ArticlesSerializer(serializers.Serializer):
    id =serializers.IntegerField(required=False)
    User =serializers.CharField(max_length=200)
    Title = serializers.CharField(max_length=200)
    Content = serializers.CharField(max_length=200)
    Category=serializers.CharField(max_length=200)
    def to_internal_value(self, data):
        if 'User' in data:
            data['User']=User.objects.get(pk=data['User'])
        if 'Category' in data:
            data['Category']=Category.objects.get(pk=data['Category'])
        return data
    def create(self, validated_data):
        return Articles.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.User = validated_data.get('User', instance.User)
        instance.Title = validated_data.get('Title', instance.Title)
        instance.Content = validated_data.get('Content', instance.Content)
        instance.Category = validated_data.get('Category', instance.Category)
        instance.save()
        return instance