
from django.urls import  path
from .userViews import  UserApiGetAll, UserApiGetById,UserInformationByToken
from .articlesViews import ArticlesApi,ArticlesApiGetById
from .categoryViews import CategoriesViewChilden,CategoriesApiAll,CategoriesApiByid,CategoriesViewParent
from .tokenViews import TokenApi
from .groupViews import GroupsApiAll

urlpatterns = [
    path('api/token/', TokenApi.as_view(), name='LoginApi'),
    path('users',UserApiGetAll.as_view()),
    path('user',UserInformationByToken.as_view()),
    path('users/<int:id>',UserApiGetById.as_view()),
    path('articles',ArticlesApi.as_view()),
    path('articles/<int:id>',ArticlesApiGetById.as_view()),
    path('categories',CategoriesApiAll.as_view()),
    path('categories/<int:id>',CategoriesApiByid.as_view()),
    path('categories/<int:id>/children',CategoriesViewChilden.as_view()),
    path('categories/<int:id>/ancestors',CategoriesViewParent.as_view()),
    path('groups',GroupsApiAll.as_view()),
]