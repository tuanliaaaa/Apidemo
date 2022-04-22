
from rest_framework import status
from rest_framework.response import Response
from .categoryModel import Category
from .userModel import User
from .articlesModel import Articles
from rest_framework.decorators import APIView
from django.utils.decorators import method_decorator
from .roleRequestDecorator import RoleRequest
class ArticlesApi(APIView):
    @method_decorator(RoleRequest(allowedRoles=['admin','Editor']))
    def get(self,request):
        articles = Articles.objects.all()
        articleJsons = []
        for article in articles:
            articleJson={'id':article.id,'UserName':article.User.UserName,'Title':article.Title,'Content':article.Content,'Category':article.Category.CategoryName}
            articleJsons.append(articleJson)
        return Response(articleJsons,status=status.HTTP_200_OK)
    @method_decorator(RoleRequest(allowedRoles=['admin','Editor']))
    def post(self,request):
        newArticle=request.data
        newArticle['Id']=request.userID
        if not 'Category'  in newArticle :
            return Response({'message':'Trường Category là bắt buộc'},status=status.HTTP_400_BAD_REQUEST)
        if not 'Content' in newArticle:
            return Response({'message':'Trường Content là bắt buộc'},status=status.HTTP_400_BAD_REQUEST)
        if not 'Title' in newArticle:
            return Response({'message':'Trường Title là bắt buộc'},status=status.HTTP_400_BAD_REQUEST)
        try:
            userAriticles = User.objects.get(pk=newArticle['Id'])
        except:
            return Response({'message':'User này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        try:
            CategoryAriticles = Category.objects.get(CategoryName=newArticle['Category'])
        except:
            return Response({'message':'Category này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        article=Articles(User=userAriticles,Title=newArticle['Title'],Content=newArticle['Content'],Category=CategoryAriticles)
        article.save()
        articleJson={'id':article.id,'UserName':article.User.UserName,'Title':article.Title,'Content':article.Content,'Category':article.Category.CategoryName}
        return Response(articleJson,status=status.HTTP_201_CREATED)

class ArticlesApiGetById(APIView):
    @method_decorator(RoleRequest(allowedRoles=['admin','Editor']))
    def get(self,request,id):
        try:
            article = Articles.objects.get(pk=id)
        except:
            return Response({'message':'Article này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        articleJson={'id':article.id,'UserName':article.User.UserName,'Title':article.Title,'Content':article.Content,'Category':article.Category.CategoryName}
        return Response(articleJson,status=status.HTTP_200_OK)
    @method_decorator(RoleRequest(allowedRoles=['admin','Editor']))
    def patch(self,request,id):
        try:
            article = Articles.objects.get(pk=id)
        except:
            return Response({'message':'Article này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        updateArticles =request.data
        if 'UserName' in updateArticles:
            try:
                user = User.objects.get(UserName=updateArticles['UserName'])
            except:
                return Response({'message':'User này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
            article.User=user
        if 'Category'  in updateArticles:
            try:
                category = Category.objects.get(CategoryName=updateArticles['Category'])
            except:
                return Response({'message':'User này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
            article.Category=category
        if 'Title' in updateArticles:
            article.Title=updateArticles['Title']
        if 'Content' in updateArticles:
            article.Content =updateArticles['Content']
        article.save()
        articleJson={'id':article.id,'UserName':article.User.UserName,'Title':article.Title,'Content':article.Content,'Category':article.Category.CategoryName}
        return Response(articleJson,status=status.HTTP_205_RESET_CONTENT)
    @method_decorator(RoleRequest(allowedRoles=['admin','Editor']))
    def delete(self,request,id):
        try:
            article = Articles.objects.get(pk=id)
        except:
            return Response({'message':'Article này không tồn tại'},status=status.HTTP_404_NOT_FOUND)
        article.delete()
        return Response({'massage':'Article đã xóa thành công'},status=status.HTTP_204_NO_CONTENT)
