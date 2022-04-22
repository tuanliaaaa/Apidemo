from this import s
from pkg_resources import require
from rest_framework import serializers
from .groupModel import Group
class GroupSerializer(serializers.Serializer):
    id =serializers.IntegerField(required=False)
    GroupName = serializers.CharField(max_length=225)
    def create(self, validated_data):
        return Group.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.GroupName = validated_data.get('GroupName', instance.GroupName)
        instance.save()
        return instance