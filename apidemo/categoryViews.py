
from rest_framework import status
from rest_framework.response import Response
from .categoryModel import Category
from datetime import datetime,timedelta,timezone
from rest_framework.decorators import APIView
from django.utils.decorators import method_decorator
from News.decorators import RoleRequest
class CategoryApiGetall(APIView):
    @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def get(self,request):
        
        ListCategories=Category.objects.all()
        ListCategoriesJson=[]
        for Categorie in ListCategories:
            CategorieJson={'id':Categorie.id,'CategoryName':Categorie.CategoryName}
            ListCategoriesJson.append(CategorieJson)
        return Response(ListCategoriesJson,status=status.HTTP_200_OK)
    @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def post(self,request):
        NewCategorie =request.data
        if not 'CategoryName' in NewCategorie:
            return Response({'message':'Trường CategoryName là bắt buộc'},status=status.HTTP_400_BAD_REQUEST)
        if not 'CategoryCodeParent' in NewCategorie:
            return Response({'message':'Trường CategoryCodeParent là bắt buộc'},status=status.HTTP_400_BAD_REQUEST)
        else:
            if not isinstance(NewCategorie['CategoryCodeParent'], int):
                return Response({'message':'Trường CategoryCodeParent là số nguyên vui lòng nhập lại'},status=status.HTTP_400_BAD_REQUEST)
            else:
                if NewCategorie['CategoryCodeParent'] < 0:
                    return Response({'message':'Trường CategoryCodeParent là số nguyên lớn hơn 0 vui lòng nhập lại'},status=status.HTTP_400_BAD_REQUEST)
        Categorie = Category(CategoryName=NewCategorie['CategoryName'],CategoryCodeParent=NewCategorie['CategoryCodeParent'])
        Categorie.save()
        CategorieJson={'id':Categorie.id,'CategoryName':Categorie.CategoryName}
        return Response(CategorieJson,status=status.HTTP_201_CREATED)

class CatrgoryApiGetByid(APIView):
    @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def get(self,request,id):
        try:
            Categorie =Category.objects.get(pk=id)
        except:
            return Response({'massage':'Categorie này không tồn tại'})
        CategorieJson={'id':Categorie.id,'CategoryName':Categorie.CategoryName}
        return Response(CategorieJson,status=status.HTTP_200_OK)
    @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def patch(self,request,id):
        try:
            Categorie =Category.objects.get(pk=id)
        except:
            return Response({'massage':'Categorie này không tồn tại'})
        UpdateCategorie =request.data
        if 'CategoryName' in UpdateCategorie:
            Categorie.CategoryName = UpdateCategorie['CategoryName']
        if 'CategoryCodeParent' in UpdateCategorie:
            Categorie.CategoryCodeParent= UpdateCategorie['CategoryCodeParent']
        Categorie.save()
        CategorieJson={'id':Categorie.id,'CategoryName':Categorie.CategoryName}
        return Response(CategorieJson,status=status.HTTP_205_RESET_CONTENT)
    @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def delete(self,request,id):
        try:
            Categorie =Category.objects.get(pk=id)
        except:
            return Response({'massage':'Categorie này không tồn tại'})
        Categorie.delete()
        return Response({'massage':'Categorie đã xóa thành công'},status=status.HTTP_204_NO_CONTENT)

class CategoriesViewChilden(APIView):
    @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def get(self,request,id):
        ListCategories = Category.objects.filter(CategoryCodeParent=id)
        ListCategoriesJson=[]
        for Categorie in ListCategories:
            CategoryJson={'id':Categorie.id,'CategoryName':Categorie.CategoryName}
            ListCategoriesJson.append(CategoryJson)
        return Response(ListCategoriesJson,status=status.HTTP_200_OK)
class CategoriesViewParent(APIView):
    @method_decorator(RoleRequest(allowedRoles=['admin',]))
    def get(self,request,id):
        ListCategoriesParent = []
        CategoryCodeParentNow = Category.objects.get(pk=id).CategoryCodeParent

        def quaylui(i):
            CategoryCheckBigger = Category.objects.get(pk=i)
            CategoryJson={'id':CategoryCheckBigger.pk,'CategoryName':CategoryCheckBigger.CategoryName}
            if CategoryCheckBigger.CategoryCodeParent!=0:
                quaylui(CategoryCheckBigger.CategoryCodeParent)
            ListCategoriesParent.append(CategoryJson)
        if CategoryCodeParentNow!=0:
            CategoryJson={'id':Category.objects.get(pk=CategoryCodeParentNow).pk,'CategoryName':Category.objects.get(pk=CategoryCodeParentNow).CategoryName}
            quaylui(CategoryJson['id'])
            return Response(ListCategoriesParent,status=status.HTTP_200_OK)
        return Response({'message':'Không có tập cha  nào cả'})
