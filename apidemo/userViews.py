from types import prepare_class
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from .userModel import User
from rest_framework.decorators import APIView
from News.decorators import RoleRequest
from rest_framework.decorators import api_view
from django.utils.decorators import method_decorator
class UserInformationByToken(APIView):
    def get(self,request):
        user= User.objects.get(pk=request.userID)
        userJson ={'id':user.id,'UserName':user.UserName,'Age':user.Age,'Email':user.Email,'GroupNames':request.groupNames}
        return Response(userJson,status=status.HTTP_200_OK)
class UserApiGetAll(APIView):  
    # @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def get(self,request):   
        ListUser = User.objects.all()
        ListUserJson = []
        for Users in ListUser:
            UserJson={'id':Users.id,'UserName':Users.UserName,'Age':Users.Age,'Email':Users.Email}
            ListUserJson.append(UserJson)
        return Response(ListUserJson,status=status.HTTP_200_OK)
    @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def post(self,request):
        NewUser = request.data
        if  not NewUser['UserName']:
            return Response({'message':'Trường UserName là bắt buộc'},status=status.HTTP_400_BAD_REQUEST)
        if not 'Age'  in NewUser :
            NewUser['Age']= 0
        if not 'Email' in NewUser:
            NewUser['Email']=''
        Users = User(UserName = NewUser['UserName'],Age=NewUser['Age'],Email=NewUser['Email'])
        Users.save()
        return Response({'id':Users.id,'UserName':Users.UserName,'Age':Users.Age,'Email':Users.Email},status=status.HTTP_201_CREATED)
    
class UserApiGetById(APIView):
    # @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def get(self,request,id):
        try:
            Users = User.objects.get(pk=id)
        except:
            return Response({'message':'User này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        UserJson={'id':Users.id,'UserName':Users.UserName,'Age':Users.Age,'Email':Users.Email}
        return Response(UserJson,status=status.HTTP_200_OK)
    @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def patch(self,request,id):
        try:
            Users = User.objects.get(pk=id)
        except:
            return Response({'message':'User này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        UpdateUser = request.data 
        if 'Age' in UpdateUser:
            Users.Age=UpdateUser['Age']
        if 'UserName' in UpdateUser:
            Users.UserName=UpdateUser['UserName']
        if 'Email' in UpdateUser:
            Users.Email= UpdateUser['Email']
        Users.save()
        UserJson={'id':Users.id,'UserName':Users.UserName,'Age':Users.Age,'Email':Users.Email}
        return Response(UserJson,status=status.HTTP_205_RESET_CONTENT)
    @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def delete(self,request,id):
        try:
            Users = User.objects.get(pk=id)
        except:
            return Response({'message':'User này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        Users.delete()
        return Response({'massage':'User đã xóa thành công'},status=status.HTTP_204_NO_CONTENT)
