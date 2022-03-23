
from django.urls import  path
from .userViews import  UserApiGetAll, UserApiGetById
from .articlesViews import ArticlesApiGetAll,ArticlesApiGetById
from .categoryViews import CategoriesViewChilden,CategoryApiGetall,CatrgoryApiGetByid,CategoriesViewParent
from .tokenViews import TokenView
from .loginViews import LoginAjax

urlpatterns = [
    path('api/token/', TokenView.as_view(), name='LoginApi'),
    path('login/',LoginAjax.as_view()),
    path('users',UserApiGetAll.as_view()),
    path('users/<int:id>',UserApiGetById.as_view()),
    path('articles',ArticlesApiGetAll.as_view()),
    path('articles/<int:id>',ArticlesApiGetById.as_view()),
    path('categories',CategoryApiGetall.as_view()),
    path('categories/<int:id>',CatrgoryApiGetByid.as_view()),
    path('categories/<int:id>/children',CategoriesViewChilden.as_view()),
    path('categories/<int:id>/ancestors',CategoriesViewParent.as_view()),

]