from types import prepare_class
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from .userModel import User
from rest_framework.decorators import APIView
from .roleRequestDecorator import RoleRequest
from rest_framework.decorators import api_view
from django.utils.decorators import method_decorator
from json import loads
class UserInformationByToken(APIView):
    def get(self,request):
        user= User.objects.get(pk=request.userID)
        userJson ={'id':user.id,'UserName':user.UserName,'Age':user.Age,'Email':user.Email,'GroupNames':request.groupNames}
        return Response(userJson,status=status.HTTP_200_OK)
class UserApiGetAll(APIView):  
    # @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def get(self,request):   
        users = User.objects.all()
        userJsons = []
        for user in users:
            userJson={'id':user.id,'UserName':user.UserName,'Age':user.Age,'Email':user.Email}
            userJsons.append(userJson)
        return Response(userJsons,status=status.HTTP_200_OK)
    @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def post(self,request):
        newUser = request.data
        if  not newUser['UserName']:
            return Response({'message':'Trường UserName là bắt buộc'},status=status.HTTP_400_BAD_REQUEST)
        if not 'Age'  in newUser :
            newUser['Age']= 0
        if not 'Email' in newUser:
            newUser['Email']=''
        user = User(UserName = newUser['UserName'],Age=newUser['Age'],Email=newUser['Email'])
        user.save()
        return Response({'id':user.id,'UserName':user.UserName,'Age':user.Age,'Email':user.Email},status=status.HTTP_201_CREATED)
    
class UserApiGetById(APIView):
    # @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def get(self,request,id):
        try:
            user = User.objects.get(pk=id)
        except:
            return Response({'message':'User này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        userJson={'id':user.id,'UserName':user.UserName,'Age':user.Age,'Email':user.Email}
        return Response(userJson,status=status.HTTP_200_OK)
    @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def patch(self,request,id):
        try:
            user = User.objects.get(pk=id)
        except:
            return Response({'message':'User này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        updateUser = request.data 
        if 'Age' in updateUser:
            user.Age=updateUser['Age']
        if 'UserName' in updateUser:
            user.UserName=updateUser['UserName']
        if 'Email' in updateUser:
            user.Email= updateUser['Email']
        user.save()
        userJson={'id':user.id,'UserName':user.UserName,'Age':user.Age,'Email':user.Email}
        return Response(userJson,status=status.HTTP_205_RESET_CONTENT)
    @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def delete(self,request,id):
        try:
            user = User.objects.get(pk=id)
        except:
            return Response({'message':'User này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response({'massage':'User đã xóa thành công'},status=status.HTTP_204_NO_CONTENT)
