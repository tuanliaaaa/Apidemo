
import imp
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from .categoryModel import Category
from .userModel import User
from .articlesModel import Articles
from rest_framework.decorators import APIView
from django.utils.decorators import method_decorator
from .roleRequestDecorator import RoleRequest
from .articlesSerializer import ArticlesSerializer
from rest_framework.parsers import JSONParser
class ArticlesApi(APIView):
    # @method_decorator(RoleRequest(allowedRoles=['admin','Editor']))
    def get(self,request):
        articles = Articles.objects.all()
        articleSerializers =ArticlesSerializer(articles,many=True)
        return Response(articleSerializers.data,status=status.HTTP_200_OK)
    # @method_decorator(RoleRequest(allowedRoles=['admin','Editor']))
    def post(self,request):
        articles = JSONParser().parse(request)
        articleSerializer = ArticlesSerializer(data=articles)
        if articleSerializer.is_valid():
            articleSerializer.save()
            return Response(articleSerializer.data, status=201)
        return Response(articleSerializer.errors, status=400)
class ArticlesApiGetById(APIView):
    def get_article(self,pk):
        try:
            return Articles.objects.get(pk=pk)
        except Articles.DoesNotExist:
            raise Http404
    # @method_decorator(RoleRequest(allowedRoles=['admin','Editor']))
    def get(self,request,id):
        article = self.get_article(id)
        articleSerializer =ArticlesSerializer(article)
        return Response(articleSerializer.data,status=status.HTTP_200_OK)
    # @method_decorator(RoleRequest(allowedRoles=['admin','Editor']))
    def patch(self,request,id):
        article = self.get_article(id)
        articleUpdate = JSONParser().parse(request)
        articleUpdateSerializer = ArticlesSerializer(article,articleUpdate,partial=True)
        if articleUpdateSerializer.is_valid():
            articleUpdateSerializer.save()
            return Response(articleUpdateSerializer.data)
        return Response(articleUpdateSerializer.errors, status=400)
    # @method_decorator(RoleRequest(allowedRoles=['admin','Editor']))
    def delete(self,request,id):
        article = self.get_article(id)
        article.delete()
        return Response({'massage':'Article đã xóa thành công'},status=status.HTTP_204_NO_CONTENT)
class ArticlesByCategory(APIView):
    def get(self,request,category):
        ariticles = Articles.objects.filter(Category__CategoryName=category)
        ariticlesSerializer=ArticlesSerializer(ariticles,many=True)
        return Response(ariticlesSerializer.data,status=200)
