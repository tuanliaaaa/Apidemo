from types import prepare_class
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response
from .categoryModel import Category
from .userModel import User
from .articlesModel import Articles
import time
import jwt
from datetime import datetime,timedelta,timezone
key="tuan"
from rest_framework.decorators import APIView

# ------------------------Start User -----------------

def CheckAuth(a,CheckArticles=0):
    try:
        
        jwt_payloadSplit=a['Authorization'].split(' ')
        jwt_payload = jwt_payloadSplit[1]
        jwt_payloadDecode=jwt.decode(jwt_payload, key, algorithms=["HS256"])
        if jwt_payloadDecode['Group']=="admin":
            return 1
        else:
            if(CheckArticles):
                print('vcl')
                return 1
            else:
                    return 0
    except:
        return 0

class TokenView(APIView):
    
    def post(self,request):
        exp=datetime.now(tz=timezone.utc) + timedelta(minutes=50)
        UserRequestToken =request.data
        if not UserRequestToken['UserName']:
            return Response({'Vui lòng nhập UserName'},status=status.HTTP_400_BAD_REQUEST)
        if not UserRequestToken['PassWord']:
            return Response({'Vui lòng nhập mật khẩu'},status=status.HTTP_400_BAD_REQUEST)
        try:
            Users= User.objects.get(UserName=UserRequestToken['UserName'],PassWord=UserRequestToken['PassWord'])
        except:
            return Response({'User này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        PayLoad = {'UserID':Users.pk,"UserName":Users.UserName,"Email":Users.Email,"Group":Users.GroupUser.GroupName,"exp":exp}
        jwt_payload = jwt.encode(PayLoad,key,)
        return Response({"access":jwt_payload},status=status.HTTP_201_CREATED)
class UserApiGetAll(APIView):    
    def get(self,request):   
        checkAuths=CheckAuth(request.headers)
        if(not checkAuths):
            return Response({"message":"bạn không có quyền truy cập"},status=status.HTTP_400_BAD_REQUEST)
        ListUser = User.objects.all()
        ListUserJson = []
        for Users in ListUser:
            UserJson={'id':Users.id,'UserName':Users.UserName,'Age':Users.Age,'Email':Users.Email}
            ListUserJson.append(UserJson)
        return Response(ListUserJson,status=status.HTTP_200_OK)
    
    def post(self,request):
        checkAuths=CheckAuth(request.headers)
        if(not checkAuths):
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
    
class UserApigetbyid(APIView):
    def get(self,request,id):
        checkAuths=CheckAuth(request.headers)
        if(not checkAuths):
            return Response({"message":"bạn không có quyền truy cập"},status=status.HTTP_400_BAD_REQUEST)
        try:
            Users = User.objects.get(pk=id)
        except:
            return Response({'message':'User này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        UserJson={'id':Users.id,'UserName':Users.UserName,'Age':Users.Age,'Email':Users.Email}
        return Response(UserJson,status=status.HTTP_200_OK)
    def patch(self,request,id):
        checkAuths=CheckAuth(request.headers)
        if(not checkAuths):
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
        checkAuths=CheckAuth(request.headers)
        if(not checkAuths):
            return Response({"message":"bạn không có quyền truy cập"},status=status.HTTP_400_BAD_REQUEST)
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
        checkAuths=CheckAuth(request.headers,1)
        if(not checkAuths):
            return Response({"message":"bạn không có quyền truy cập"},status=status.HTTP_400_BAD_REQUEST)
        ListArticles = Articles.objects.all()
        ListArticlesJson = []
        for Article in ListArticles:
            ArticleJson={'id':Article.id,'UserName':Article.User.UserName,'Title':Article.Title,'Content':Article.Content,'Category':Article.Category.CategoryName}
            ListArticlesJson.append(ArticleJson)
        return Response(ListArticlesJson,status=status.HTTP_200_OK)
    def post(self,request):
        checkAuths=CheckAuth(request.headers)
        if(not checkAuths):
           return Response({"message":"bạn không có quyền truy cập"},status=status.HTTP_400_BAD_REQUEST)
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
        checkAuths=CheckAuth(request.headers,1)
        if(not checkAuths):
            return Response({"message":"bạn không có quyền truy cập"},status=status.HTTP_400_BAD_REQUEST)
        try:
            Article = Articles.objects.get(pk=id)
        except:
            return Response({'message':'Article này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        ArticleJson={'id':Article.id,'UserName':Article.User.UserName,'Title':Article.Title,'Content':Article.Content,'Category':Article.Category.CategoryName}
        return Response(ArticleJson,status=status.HTTP_200_OK)
    def patch(self,request,id):
        checkAuths=CheckAuth(request.headers,1)
        if(not checkAuths):
            return Response({"message":"bạn không có quyền truy cập"},status=status.HTTP_400_BAD_REQUEST)
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
        checkAuths=CheckAuth(request.headers,1)
        if(not checkAuths):
            return Response({"message":"bạn không có quyền truy cập"},status=status.HTTP_400_BAD_REQUEST)
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
        checkAuths=CheckAuth(request.headers)
        if(not checkAuths):
            return Response({"message":"bạn không có quyền truy cập"},status=status.HTTP_400_BAD_REQUEST)
        ListCategories=Category.objects.all()
        ListCategoriesJson=[]
        for Categorie in ListCategories:
            CategorieJson={'id':Categorie.id,'CategoryName':Categorie.CategoryName}
            ListCategoriesJson.append(CategorieJson)
        return Response(ListCategoriesJson,status=status.HTTP_200_OK)
    def post(self,request):
        checkAuths=CheckAuth(request.headers)
        if(not checkAuths):
            return Response({"message":"bạn không có quyền truy cập"},status=status.HTTP_400_BAD_REQUEST)
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
        checkAuths=CheckAuth(request.headers)
        if(not checkAuths):
            return Response({"message":"bạn không có quyền truy cập"},status=status.HTTP_400_BAD_REQUEST)
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
        checkAuths=CheckAuth(request.headers)
        if(not checkAuths):
            return Response({"message":"bạn không có quyền truy cập"},status=status.HTTP_400_BAD_REQUEST)
        ListCategories = Category.objects.filter(CategoryCodeParent=id)
        ListCategoriesJson=[]
        for Categorie in ListCategories:
            CategoryJson={'id':Categorie.id,'CategoryName':Categorie.CategoryName}
            ListCategoriesJson.append(CategoryJson)
        return Response(ListCategoriesJson,status=status.HTTP_200_OK)
class CategoriesViewParent(APIView):
    def get(self,request,id):
        checkAuths=CheckAuth(request.headers)
        if(not checkAuths):
            return Response({"message":"bạn không có quyền truy cập"},status=status.HTTP_400_BAD_REQUEST)
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