from http.client import HTTPResponse
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from .userModel import User
from  News.settings import key
import jwt
import json
from datetime import datetime,timedelta,timezone
from rest_framework.decorators import APIView
from django.views import View
from .groupUserModel import GroupUser
class TokenView(View):
    def post(self,request):
        exp=datetime.now(tz=timezone.utc) + timedelta(minutes=50)
        userRequestTokenJson =request.body
        userRequestToken=json.loads(userRequestTokenJson)
        if 'UserName' not in userRequestToken or not userRequestToken['UserName']:
            return HttpResponse('{"massage":"Vui lòng nhập UserName"}',status=status.HTTP_400_BAD_REQUEST)
        if 'PassWord' not in userRequestToken or not userRequestToken['PassWord']:
            return HttpResponse('{"massage":"Vui lòng nhập mật khẩu"}',status=status.HTTP_400_BAD_REQUEST)
        try:
            users= User.objects.get(UserName=userRequestToken['UserName'],PassWord=userRequestToken['PassWord'])
        except:
            return HttpResponse('{"massage":"User này không tồn tại"}',status=status.HTTP_404_NOT_FOUND)
        groupsName=[]
        groupUsers=GroupUser.objects.filter(User=users)
        for gruopUser in groupUsers:
            groupsName.append(gruopUser.Group.GroupName)
        payLoad = {'UserID':users.pk,"UserName":users.UserName,"Email":users.Email,"Group":groupsName,"exp":exp}
        jwtToken = jwt.encode(payLoad,key,) 
        jwtTokenUser={"access":jwtToken}
        jwtTokenJson = json.dumps(jwtTokenUser)
        return HttpResponse(jwtTokenJson,status=status.HTTP_200_OK)
        
        
