from types import prepare_class
from rest_framework import status
from rest_framework.response import Response
from .userModel import User
from rest_framework.decorators import APIView
from .checkAuthViews import CheckAuth
class UserApiGetAll(APIView):    
    def get(self,request):   
        isAuthenticated=CheckAuth(request.headers)
        if(not isAuthenticated):
            return Response({"message":"bạn không có quyền truy cập"},status=status.HTTP_400_BAD_REQUEST)
        ListUser = User.objects.all()
        ListUserJson = []
        for Users in ListUser:
            UserJson={'id':Users.id,'UserName':Users.UserName,'Age':Users.Age,'Email':Users.Email}
            ListUserJson.append(UserJson)
        return Response(ListUserJson,status=status.HTTP_200_OK)
    
    def post(self,request):
        isAuthenticated=CheckAuth(request.headers)
        if(not isAuthenticated):
            return Response({"message":"bạn không có quyền truy cập"},status=status.HTTP_400_BAD_REQUEST)
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
    def get(self,request,id):
        isAuthenticated=CheckAuth(request.headers)
        if(not isAuthenticated):
            return Response({"message":"bạn không có quyền truy cập"},status=status.HTTP_400_BAD_REQUEST)
        try:
            Users = User.objects.get(pk=id)
        except:
            return Response({'message':'User này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        UserJson={'id':Users.id,'UserName':Users.UserName,'Age':Users.Age,'Email':Users.Email}
        return Response(UserJson,status=status.HTTP_200_OK)
    def patch(self,request,id):
        isAuthenticated=CheckAuth(request.headers)
        if(not isAuthenticated):
           return Response({"message":"bạn không có quyền truy cập"},status=status.HTTP_400_BAD_REQUEST)
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
    def delete(self,request,id):
        isAuthenticated=CheckAuth(request.headers)
        if(not isAuthenticated):
            return Response({"message":"bạn không có quyền truy cập"},status=status.HTTP_400_BAD_REQUEST)
        try:
            Users = User.objects.get(pk=id)
        except:
            return Response({'message':'User này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        Users.delete()
        return Response({'massage':'User đã xóa thành công'},status=status.HTTP_204_NO_CONTENT)
