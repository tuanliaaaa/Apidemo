from types import prepare_class
from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response
from .models import User, Articles,Category
from rest_framework import permissions
from rest_framework.decorators import APIView

# ------------------------Start User -----------------

class UserApiGetAll(APIView):
    
    def get(self,request):
        
        ListUser = User.objects.all()
        ListUserJson = []
        for Users in ListUser:
            UserJson={'id':Users.id,'UserName':Users.UserName,'Age':Users.Age,'Email':Users.Email}
            ListUserJson.append(UserJson)
        return Response(ListUserJson,status=status.HTTP_200_OK)
    
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
    
class UserApigetbyid(APIView):
    def get(self,request,id):
        try:
            Users = User.objects.get(pk=id)
        except:
            return Response({'message':'User này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        UserJson={'id':Users.id,'UserName':Users.UserName,'Age':Users.Age,'Email':Users.Email}
        return Response(UserJson,status=status.HTTP_200_OK)
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
    def delete(self,request,id):
        try:
            Users = User.objects.get(pk=id)
        except:
            return Response({'message':'User này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        Users.delete()
        return Response({'massage':'User đã xóa thành công'},status=status.HTTP_204_NO_CONTENT)

# ------------------- End User ------------------------

# ---------------------Start Articles -----------------

class ArticlesApiGetAll(APIView):
    def get(self,request):
        ListArticles = Articles.objects.all()
        ListArticlesJson = []
        for Article in ListArticles:
            ArticleJson={'id':Article.id,'UserName':Article.User.UserName,'Title':Article.Title,'Content':Article.Content,'Category':Article.Category.CategoryName}
            ListArticlesJson.append(ArticleJson)
        return Response(ListArticlesJson,status=status.HTTP_200_OK)
    def post(self,request):
        NewArticles
        if  not 'UserName' in NewArticles:
            return Response({'message':'Trường UserName là bắt buộc'},status=status.HTTP_400_BAD_REQUEST)
        if not 'Category'  in NewArticles :
            return Response({'message':'Trường Category là bắt buộc'},status=status.HTTP_400_BAD_REQUEST)
        if not 'Content' in NewArticles:
            return Response({'message':'Trường Content là bắt buộc'},status=status.HTTP_400_BAD_REQUEST)
        if not 'Title' in NewArticles:
            return Response({'message':'Trường Title là bắt buộc'},status=status.HTTP_400_BAD_REQUEST)
        try:
            UserAriticles = User.objects.get(UserName=NewArticles['UserName'])
        except:
            return Response({'message':'User này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        try:
            CategoryAriticles = Category.objects.get(CategoryName=NewArticles['Category'])
        except:
            return Response({'message':'Category này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        Article=Articles(User=UserAriticles,Title=NewArticles['Title'],Content=NewArticles['Content'],Category=CategoryAriticles)
        Article.save()
        ArticleJson={'id':Article.id,'UserName':Article.User.UserName,'Title':Article.Title,'Content':Article.Content,'Category':Article.Category.CategoryName}
        return Response(ArticleJson,status=status.HTTP_201_CREATED)

class ArticlesApiGetById(APIView):
    def get(self,request,id):
        try:
            Article = Articles.objects.get(pk=id)
        except:
            return Response({'message':'Article này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        ArticleJson={'id':Article.id,'UserName':Article.User.UserName,'Title':Article.Title,'Content':Article.Content,'Category':Article.Category.CategoryName}
        return Response(ArticleJson,status=status.HTTP_200_OK)
    def patch(self,request,id):
        try:
            Article = Articles.objects.get(pk=id)
        except:
            return Response({'message':'Article này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        UpdateArticles =request.data
        if 'UserName' in UpdateArticles:
            try:
                Users = User.objects.get(UserName=UpdateArticles['UserName'])
            except:
                return Response({'message':'User này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
            Article.User=Users
        if 'Category'  in UpdateArticles:
            try:
                Categories = Category.objects.get(CategoryName=UpdateArticles['Category'])
            except:
                return Response({'message':'User này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
            Article.Category=Categories
        if 'Title' in UpdateArticles:
            Article.Title=UpdateArticles['Title']
        if 'Content' in UpdateArticles:
            Article.Content =UpdateArticles['Content']
        Article.save()
        ArticleJson={'id':Article.id,'UserName':Article.User.UserName,'Title':Article.Title,'Content':Article.Content,'Category':Article.Category.CategoryName}
        return Response(ArticleJson,status=status.HTTP_205_RESET_CONTENT)
    def delete(self,request,id):
        try:
            Article = Articles.objects.get(pk=id)
        except:
            return Response({'message':'Article này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        Article.delete()
        return Response({'massage':'Article đã xóa thành công'},status=status.HTTP_204_NO_CONTENT)

# ----------------- End Articles ----------------------

# ---------------------Start Category -----------------

class CategoryApiGetall(APIView):
    def get(self,request):
        ListCategories=Category.objects.all()
        ListCategoriesJson=[]
        for Categorie in ListCategories:
            CategorieJson={'id':Categorie.id,'CategoryName':Categorie.CategoryName}
            ListCategoriesJson.append(CategorieJson)
        return Response(ListCategoriesJson,status=status.HTTP_200_OK)
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
    def get(self,request,id):
        try:
            Categorie =Category.objects.get(pk=id)
        except:
            return Response({'massage':'Categorie này không tồn tại'})
        CategorieJson={'id':Categorie.id,'CategoryName':Categorie.CategoryName}
        return Response(CategorieJson,status=status.HTTP_200_OK)
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
    def delete(self,request,id):
        try:
            Categorie =Category.objects.get(pk=id)
        except:
            return Response({'massage':'Categorie này không tồn tại'})
        Categorie.delete()
        return Response({'massage':'Categorie đã xóa thành công'},status=status.HTTP_204_NO_CONTENT)

class CategoriesViewChilden(APIView):
    def get(self,request,id):
        ListCategories = Category.objects.filter(CategoryCodeParent=id)
        ListCategoriesJson=[]
        for Categorie in ListCategories:
            CategoryJson={'id':Categorie.id,'CategoryName':Categorie.CategoryName}
            ListCategoriesJson.append(CategoryJson)
        return Response(ListCategoriesJson,status=status.HTTP_200_OK)
class CategoriesViewParent(APIView):
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
# ----------------- End Category ----------------------