from turtle import st
from rest_framework import status
from rest_framework.response import Response
from .categoryModel import Category
from datetime import datetime,timedelta,timezone
from rest_framework.decorators import APIView
from django.utils.decorators import method_decorator
from News.decorators import RoleRequest
from .groupModel import Group
class GroupApiGetAll(APIView):
    def get(self,request):
        groups= Group.objects.all()
        listGroup=[]
        for group in groups:
            dictGroup={'id':group.pk,'GroupName':group.GroupName}
            listGroup.append(dictGroup)
        return Response(listGroup,status=status.HTTP_200_OK)