from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import  path

from .views import ArticlesApiGetAll, UserApiGetAll, UserApigetbyid,ArticlesApiGetById,CategoryApiGetall,CatrgoryApiGetByid,CategoriesViewChilden,CategoriesViewParent
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users',UserApiGetAll.as_view()),
    path('users/<int:id>',UserApigetbyid.as_view()),
    path('articles',ArticlesApiGetAll.as_view()),
    path('articles/<int:id>',ArticlesApiGetById.as_view()),
    path('categories',CategoryApiGetall.as_view()),
    path('categories/<int:id>',CatrgoryApiGetByid.as_view()),
    path('categories/<int:id>/children',CategoriesViewChilden.as_view()),
    path('categories/<int:id>/ancestors',CategoriesViewParent.as_view()),

]