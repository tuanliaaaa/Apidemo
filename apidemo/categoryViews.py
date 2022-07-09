
from re import I
from unicodedata import category
from django.http import HttpResponse
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from .categorySerializer import CategorySerializer
from .categoryModel import Category
from datetime import datetime,timedelta,timezone
from rest_framework.decorators import APIView
from django.utils.decorators import method_decorator
from .roleRequestDecorator import RoleRequest
from rest_framework.parsers import JSONParser
class CategoriesApiAll(APIView):
    @method_decorator(RoleRequest(allowedRoles=['Admin',]))
    def get(self,request):
        categories = Category.objects.all()
        categorySerializer = CategorySerializer(categories,many=True)
        return Response(categorySerializer.data,status=status.HTTP_200_OK)
    # @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def post(self,request):
        category = JSONParser().parse(request)
        categorySerializer = CategorySerializer(data=category)
        if categorySerializer.is_valid():
            categorySerializer.save()
            return Response(categorySerializer.data, status=201)
        return Response(categorySerializer.errors, status=400)
class CategoriesApiByid(APIView):
    def get_category(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404
    # @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def get(self,request,id):
        category = self.get_category(id)
        categorySerializer = CategorySerializer(category)
        return Response(categorySerializer.data,status=status.HTTP_200_OK)
    # @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def patch(self,request,id):
        category=self.get_category(id)
        categoryUpdate = JSONParser().parse(request)
        categoryUpdateserializer = CategorySerializer(category, data=categoryUpdate,partial=True)
        if categoryUpdateserializer.is_valid():
            categoryUpdateserializer.save()
            return Response(categoryUpdateserializer.data,status=200)
        return Response(categoryUpdateserializer.errors, status=400)
    # @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def delete(self,request,id):
        category = self.get_category(id)
        category.delete()
        return Response({'massage':'Categorie đã xóa thành công'},status=status.HTTP_204_NO_CONTENT)
class CategoriesViewChilden(APIView):
    # @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def get(self,request,id):
        categories = Category.objects.filter(CategoryCodeParent=id)
        categorySerializer =CategorySerializer(categories,many=True)
        return Response(categorySerializer.data,status=status.HTTP_200_OK)
class CategoriesViewParent(APIView):
    # @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def get(self,request,id):
        categoriesParent = []
        categoryCodeParentNow = Category.objects.get(pk=id).CategoryCodeParent
        def ListCategoriesParent(i):
            categoryCheckBigger = Category.objects.get(pk=i)
            categoryJson={'id':categoryCheckBigger.pk,'CategoryName':categoryCheckBigger.CategoryName}
            if categoryCheckBigger.CategoryCodeParent!=0:
                ListCategoriesParent(categoryCheckBigger.CategoryCodeParent)
            categoriesParent.append(categoryJson)
        if categoryCodeParentNow!=0:
            categoryJson={'id':Category.objects.get(pk=categoryCodeParentNow).pk,'CategoryName':Category.objects.get(pk=categoryCodeParentNow).CategoryName}
            ListCategoriesParent(categoryJson['id'])
            return Response(ListCategoriesParent,status=status.HTTP_200_OK)
        return Response({'message':'Không có tập cha  nào cả'})
class CatrgoriesTreeView(APIView):
    def get(self,request):
        categories = Category.objects.filter(CategoryCodeParent=0)
        listCategory=[]
        def categoriesRelation(categories,listparent):
            for category in categories:            
                childrenCategory= Category.objects.filter(CategoryCodeParent=category.pk)
                if(childrenCategory):
                    parent=[]
                    listparent.append({"name":category.CategoryName,"parent":parent})
                    categoriesRelation(childrenCategory,parent)
                else:
                    listparent.append({"name":category.CategoryName})
        categoriesRelation(categories,listCategory)
        return Response(listCategory,status=200)