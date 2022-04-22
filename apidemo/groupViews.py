from turtle import st
from rest_framework import status
from rest_framework.response import Response
from .categoryModel import Category
from datetime import datetime,timedelta,timezone
from rest_framework.decorators import APIView
from django.utils.decorators import method_decorator
from .roleRequestDecorator import RoleRequest
from .groupModel import Group
from .groupSerializer import GroupSerializer
class GroupsApiAll(APIView):
    def get(self,request):
        groups= Group.objects.all()
        groupSerializer=GroupSerializer(groups,many=True)
        return Response(groupSerializer.data,status=status.HTTP_200_OK)