
from django.urls import  path
from .userViews import  UserApiGetAll, UserApiGetById,UserInformationByToken
from .articlesViews import ArticlesApi,ArticlesApiGetById,ArticlesByCategory
from .categoryViews import CategoriesViewChilden,CategoriesApiAll,CategoriesApiByid,CategoriesViewParent, CatrgoriesTreeView
from .tokenViews import TokenApi
from .groupViews import GroupsApiAll
from .userGroupViews import GetUserAndGroupOfUser

urlpatterns = [
    path('api/token/', TokenApi.as_view(), name='LoginApi'),
    path('users',UserApiGetAll.as_view(),name='UserApiGetAll'),
    path('user',UserInformationByToken.as_view(),name='UserInformationByToken'),
    path('users/<int:id>',UserApiGetById.as_view(),name='UserApiGetById'),
    path('articles',ArticlesApi.as_view(),name='Articles'),
    path('articles/<int:id>',ArticlesApiGetById.as_view(),name='ArticlesById'),
    path('articles/<str:category>',ArticlesByCategory.as_view(),name='ArticlesByCategory'),
    path('categories',CategoriesApiAll.as_view(),name='CategoriesApiAll'),
    path('categories/treeview',CatrgoriesTreeView.as_view(),name='CatrgoriesTreeView'),
    path('categories/<int:id>',CategoriesApiByid.as_view(),name='CategoriesApiByid'),
    path('categories/<int:id>/children',CategoriesViewChilden.as_view(),name='CategoriesViewChilden'),
    path('categories/<int:id>/ancestors',CategoriesViewParent.as_view(),name='CategoriesViewParent'),
    path('groups',GroupsApiAll.as_view(),name='GroupsApiAll'),
    path('userandgroupuser',GetUserAndGroupOfUser.as_view(),name='GetUserAndGroupOfUser'),
]