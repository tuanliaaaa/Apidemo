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
from json import loads
from django.http import Http404
from rest_framework.parsers import JSONParser
class UserInformationByToken(APIView):
    # @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def get(self,request):
        try:
            user= User.objects.get(pk=request.userID)
        except:
            return Response({'message':'User này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        userSerializer = UserSerializer(user)
        return Response(userSerializer.data,status=status.HTTP_200_OK)
class UserApiGetAll(APIView):  
    # @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def get(self,request):   
        users = User.objects.all()
        userSerializers = UserSerializer(users,many=True)
        return Response(userSerializers.data,status=status.HTTP_200_OK)
    # @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def post(self,request):
        user = JSONParser().parse(request)
        userSerializer = UserSerializer(data=user)
        if userSerializer.is_valid():
            userSerializer.save()
            return Response(userSerializer.data, status=201)
        return Response(userSerializer.errors, status=400)
class UserApiGetById(APIView):
    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    # @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def get(self,request,id):
        user = self.get_user(id)
        print('dax vasldfa')
        userSerializer = UserSerializer(user)
        return Response(userSerializer.data,status=status.HTTP_200_OK)
    # @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def patch(self,request,id):
        user = self.get_user(id)
        userUpdate = JSONParser().parse(request)
        userUpdateSerializer = UserSerializer(user, data=userUpdate,partial=True)
        if userUpdateSerializer.is_valid():
            userUpdateSerializer.save()
            return Response(userUpdateSerializer.data)
        return Response(userUpdateSerializer.errors, status=400)
    # @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def delete(self,request,id):
        user = self.get_user(id)
        user.delete()
        return Response({'massage':'User đã xóa thành công'},status=status.HTTP_204_NO_CONTENT)
