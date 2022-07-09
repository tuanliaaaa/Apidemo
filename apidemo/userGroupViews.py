from types import prepare_class
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from .userModel import User
from rest_framework.decorators import APIView
from .roleRequestDecorator import RoleRequest
from rest_framework.decorators import api_view
from django.utils.decorators import method_decorator
from .userSerializer import UserSerializer
from .groupModel import Group
from json import loads
from .groupUserModel import GroupUser
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from rest_framework.parsers import JSONParser
from .userModel import User
class GetUserAndGroupOfUser(APIView):
    def get(self,request):
        users= User.objects.all()
        listGroupOfUser=[]
        for user in users:
            listGroupUser=[]
            groupUsers = GroupUser.objects.filter(User=user)
            for groupuser in groupUsers:
                listGroupUser.append(groupuser.Group.GroupName)
            listGroupOfUser.append({'UserName':user.UserName,'ListGroup':listGroupUser})
        return Response(listGroupOfUser,status=200)
    def post(self,request):
        userGroups=request.data
        listGroupinDataBase =[]
        groups=Group.objects.all()
        for group in groups:
            listGroupinDataBase.append(group.GroupName)
        user = User.objects.get(UserName=userGroups['UserName'])
        for groupName in userGroups['ListGroup']:
            group = Group.objects.get(GroupName=groupName)
            try:
                userGroup = GroupUser.objects.get(Group=group,User=user)
            except:
                userGroup=GroupUser(Group=group,User=user)
                userGroup.save()
        for group in listGroupinDataBase:
            if group not in userGroups['ListGroup']:
                try:
                    groups = Group.objects.get(GroupName=group)
                    userGroup = GroupUser.objects.get(Group=groups,User=user)
                    userGroup.delete()
                except:
                    pass
        return Response(userGroups,status=200)
        