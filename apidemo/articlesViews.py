
from rest_framework import status
from rest_framework.response import Response
from .categoryModel import Category
from .userModel import User
from .articlesModel import Articles
from rest_framework.decorators import APIView
from django.utils.decorators import method_decorator
from News.decorators import RoleRequest
class ArticlesApiGetAll(APIView):
    @method_decorator(RoleRequest(allowedRoles=['admin','Editor']))
    def get(self,request):
        articles = Articles.objects.all()
        articleViewModel = []
        for article in articles:
            articleJson={'id':article.id,'UserName':article.User.UserName,'Title':article.Title,'Content':article.Content,'Category':article.Category.CategoryName}
            articleViewModel.append(articleJson)
        return Response(articleViewModel,status=status.HTTP_200_OK)
    @method_decorator(RoleRequest(allowedRoles=['admin','Editor']))
    def post(self,request):
        NewArticles=request.data
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
    @method_decorator(RoleRequest(allowedRoles=['admin','Editor']))
    def get(self,request,id):
        try:
            Article = Articles.objects.get(pk=id)
        except:
            return Response({'message':'Article này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        ArticleJson={'id':Article.id,'UserName':Article.User.UserName,'Title':Article.Title,'Content':Article.Content,'Category':Article.Category.CategoryName}
        return Response(ArticleJson,status=status.HTTP_200_OK)
    @method_decorator(RoleRequest(allowedRoles=['admin','Editor']))
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
    @method_decorator(RoleRequest(allowedRoles=['admin','Editor']))
    def delete(self,request,id):
        try:
            Article = Articles.objects.get(pk=id)
        except:
            return Response({'message':'Article này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        Article.delete()
        return Response({'massage':'Article đã xóa thành công'},status=status.HTTP_204_NO_CONTENT)
