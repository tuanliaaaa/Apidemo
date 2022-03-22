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
from django.views.decorators.csrf import csrf_exempt
class TokenView(APIView):
    @csrf_exempt
    def post(self,request):
        
        exp=datetime.now(tz=timezone.utc) + timedelta(minutes=50)
        userRequestToken =request.data       
        if 'UserName' not in userRequestToken or not userRequestToken['UserName']:
            
            return Response({"message":"Vui lòng nhập UserName"},status=status.HTTP_400_BAD_REQUEST)
        if 'PassWord' not in userRequestToken or not userRequestToken['PassWord']:
            return Response({"message":"Vui lòng nhập Password"},status=status.HTTP_400_BAD_REQUEST)
        try:
            users= User.objects.get(UserName=userRequestToken['UserName'],PassWord=userRequestToken['PassWord'])
        except:
            
            return Response({"message":"User này không tồn tại"},status=status.HTTP_404_NOT_FOUND)
        groupNames=[]
        groupUsers=GroupUser.objects.filter(User=users)
        for gruopUser in groupUsers:
            groupNames.append(gruopUser.Group.GroupName)
        payLoad = {'UserID':users.pk,"UserName":users.UserName,"Email":users.Email,"Group":groupNames,"exp":exp}
        jwtToken = jwt.encode(payLoad,key,) 
        jwtTokenUser={"access":jwtToken}
        return Response(jwtTokenUser,status=status.HTTP_200_OK)
        
        
