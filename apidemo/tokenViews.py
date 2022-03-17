from rest_framework import status
from rest_framework.response import Response
from .userModel import User
from  News.settings import key
import jwt
from datetime import datetime,timedelta,timezone
from rest_framework.decorators import APIView


class TokenView(APIView):
    def post(self,request):
        exp=datetime.now(tz=timezone.utc) + timedelta(minutes=50)
        userRequestToken =request.data
        if not userRequestToken['UserName']:
            return Response({'Vui lòng nhập UserName'},status=status.HTTP_400_BAD_REQUEST)
        if not userRequestToken['PassWord']:
            return Response({'Vui lòng nhập mật khẩu'},status=status.HTTP_400_BAD_REQUEST)
        try:
            users= User.objects.get(UserName=userRequestToken['UserName'],PassWord=userRequestToken['PassWord'])
        except:
            return Response({'User này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        payload = {'UserID':users.pk,"UserName":users.UserName,"Email":users.Email,"Group":users.GroupUser.GroupName,"exp":exp}
        jwt_payload = jwt.encode(payload,key,)
        return Response({"access":jwt_payload},status=status.HTTP_201_CREATED)
