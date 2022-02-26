from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response
from .models import User, Post,Category
from .serializers import Useripa, Categoryipa,Articlessipa
from rest_framework.decorators import api_view

# ------------Start User ------------
@api_view(['GET', 'POST'])
def UserapiView(request):
    if request.method == 'GET':
        ListUser = User.objects.all()
        ListUser_data = Useripa(ListUser, many=True)
        return Response(data=ListUser_data.data, )
    elif request.method == 'POST':
        Users= JSONParser().parse(request)
        UserData = Useripa(data=Users)
        if UserData.is_valid():        
            UserData.save()
            return Response(data=UserData.data, status=status.HTTP_201_CREATED) 
        return Response(data=UserData.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PATCH','DELETE'])
def UserapiViewId(request,id):
    try:
        Users = User.objects.get(pk=id) 
    except:
        return Response({'message':'không tìm thấy người dùng này'},)
    if request.method == 'GET':
        UsersData = Useripa(Users)
        return Response(data=UsersData.data)
    elif request.method == 'PATCH':
        UsersPatch = JSONParser().parse(request)
        UsersData = Useripa(Users,data=UsersPatch)
        if UsersData.is_valid():
            UsersData.save()
            return Response(data=UsersData.data, status=status.HTTP_201_CREATED) 
        return Response(data=UsersData.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Users.delete() 
        return Response({'message':'Đã xóa thành công người dùng này'},)

# ------------ End User--------------

# -------------Articles--------------
@api_view(['GET', 'POST'])
def ArticlesView(request):
    if request.method == 'GET':
        Articless = Post.objects.all()
        ArticlessData = Articlessipa(Articless,many=True)
        return Response(data=ArticlessData.data,)
    if request.method == 'POST':
        Articless = JSONParser().parse(request)
        ArticlessData = Articlessipa(data=Articless)
        if ArticlessData.is_valid():
            ArticlessData.save()
            return Response(data=ArticlessData.data)
        return Response(data=ArticlessData.errors)
@api_view(['GET', 'PATCH','DELETE'])
def ArticlesViewId(request,id):
    try:
        Articless = Post.objects.get(pk=id)
    except:
        return Response({'message':'Không tìm thấy bài báo này'},)
    if request.method == 'GET':
        ArticlessData = Articlessipa(Articless)
        return Response(data=ArticlessData.data,)
    elif request.method == 'PATCH':
        ArticlessPost = JSONParser().parse(request)
        ArticlessData = Articlessipa(Articless,data=ArticlessPost)
        if ArticlessData.is_valid():
            ArticlessData.save()
            return Response(data=ArticlessData.data)
        return Response(data=ArticlessData.errors)
    elif request.method =='DELETE':
        Articless.delete()
        return Response({'message':'Bài báo này đã bị xóa'},)
# ------------ End Articles-----------

# -------------Category---------------
@api_view(['GET', 'POST'])
def CategoriesView(request):
    if request.method == 'GET':
        Categories = Category.objects.all()
        CategoriesData = Categoryipa(Categories,many=True)
        return Response(data=CategoriesData.data,)
    elif request.method == 'POST':
        Categories = JSONParser().parse(request)
        CategoriesData = Categoryipa(data=Categories)
        if CategoriesData.is_valid():
            CategoriesData.save()
            return Response(data=CategoriesData.data,)
        return Response(data=CategoriesData.errors,)
@api_view(['GET', 'PATCH','DELETE'])
def CategoriesViewID(request,id):
    try:
        Categories = Category.objects.get(pk=id)
    except:
        return Response({'message':'Không tìm thấy thể loại này'},)
    if request.method == 'GET':
        CategoriesData = Categoryipa(Categories)

        return Response(data= CategoriesData.data,)
    elif request.method == 'PATCH':
        Categorys = JSONParser().parse(request)
        CategoriesData = Categoryipa(Categories,data=Categorys)
        if CategoriesData.is_valid():
            CategoriesData.save()
            return Response(data=CategoriesData.data,)
        return Response(data= CategoriesData.errors,)
    elif request.method =='DELETE':
        Categories.delete()
        return Response({'message':'Thể loại này đã được xóa'},)
@api_view(['GET'])
def CategoriesViewParent(request,id):
    b = []
    c = Category.objects.get(pk=id).CategoryCodeParent

    def quaylui(i):
        a = Category.objects.get(pk=i)
        h={'id':a.pk,'CategoryName':a.CategoryName}
        if a.CategoryCodeParent!=0:
            quaylui(a.CategoryCodeParent)
        b.append(h)
    if c!=0:
        h={'id':Category.objects.get(pk=c).pk,'CategoryName':Category.objects.get(pk=c).CategoryName}
        quaylui(h['id'])
        return Response(b,)
    return Response({'message':'Không có tập cha  nào cả'})
@api_view(['GET'])
def CategoriesViewChilden(request,id):
    b = []
    def quaylui(i):
        a= Category.objects.filter(CategoryCodeParent=i)
        for j in a:
            h={'id':j.pk,'CategoryName':j.CategoryName}
            b.append(h)
            quaylui(j.pk)
    quaylui(id)     
    if len(b)>0:  
        return Response(b,)
    return Response({'message':'khong có con nào cả'},)

# ------------ End Category------------
    

       
        


