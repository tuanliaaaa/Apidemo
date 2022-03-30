
from rest_framework import status
from rest_framework.response import Response
from .categoryModel import Category
from datetime import datetime,timedelta,timezone
from rest_framework.decorators import APIView
from django.utils.decorators import method_decorator
from .roleRequestDecorator import RoleRequest
class CategoriesApiAll(APIView):
    @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def get(self,request):
        categories=Category.objects.all()
        categoryJsons=[]
        for category in categories:
            categoryJson={'id':category.id,'CategoryName':category.CategoryName}
            categoryJsons.append(categoryJson)
        return Response(categoryJsons,status=status.HTTP_200_OK)
    @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def post(self,request):
        newCategory =request.data
        if not 'CategoryName' in newCategory:
            return Response({'message':'Trường CategoryName là bắt buộc'},status=status.HTTP_400_BAD_REQUEST)
        if not 'CategoryCodeParent' in newCategory:
            return Response({'message':'Trường CategoryCodeParent là bắt buộc'},status=status.HTTP_400_BAD_REQUEST)
        else:
            if not isinstance(newCategory['CategoryCodeParent'], int):
                return Response({'message':'Trường CategoryCodeParent là số nguyên vui lòng nhập lại'},status=status.HTTP_400_BAD_REQUEST)
            else:
                if newCategory['CategoryCodeParent'] < 0:
                    return Response({'message':'Trường CategoryCodeParent là số nguyên lớn hơn 0 vui lòng nhập lại'},status=status.HTTP_400_BAD_REQUEST)
        category = Category(CategoryName=newCategory['CategoryName'],CategoryCodeParent=newCategory['CategoryCodeParent'])
        category.save()
        categoryJson={'id':category.id,'CategoryName':category.CategoryName}
        return Response(categoryJson,status=status.HTTP_201_CREATED)
class CategoriesApiByid(APIView):
    @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def get(self,request,id):
        try:
            category =Category.objects.get(pk=id)
        except:
            return Response({'massage':'Categorie này không tồn tại'})
        categoyJson={'id':category.id,'CategoryName':category.CategoryName}
        return Response(categoyJson,status=status.HTTP_200_OK)
    @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def patch(self,request,id):
        try:
            category =Category.objects.get(pk=id)
        except:
            return Response({'massage':'Categorie này không tồn tại'})
        updateCategory =request.data
        if 'CategoryName' in updateCategory:
            category.CategoryName = updateCategory['CategoryName']
        if 'CategoryCodeParent' in updateCategory:
            category.CategoryCodeParent= updateCategory['CategoryCodeParent']
        category.save()
        categoryJson={'id':category.id,'CategoryName':category.CategoryName}
        return Response(categoryJson,status=status.HTTP_205_RESET_CONTENT)
    @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def delete(self,request,id):
        try:
            category =Category.objects.get(pk=id)
        except:
            return Response({'massage':'Categorie này không tồn tại'})
        category.delete()
        return Response({'massage':'Categorie đã xóa thành công'},status=status.HTTP_204_NO_CONTENT)

class CategoriesViewChilden(APIView):
    @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def get(self,request,id):
        categories = Category.objects.filter(CategoryCodeParent=id)
        categoryJsons=[]
        for categorie in categories:
            categoryJson={'id':categorie.id,'CategoryName':categorie.CategoryName}
            categoryJsons.append(categoryJson)
        return Response(categoryJsons,status=status.HTTP_200_OK)
class CategoriesViewParent(APIView):
    @method_decorator(RoleRequest(allowedRoles=['admin',]))
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
