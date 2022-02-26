from django.urls import path
from . import views
urlpatterns = [
    path('users',views.UserapiView),
    path('users/<int:id>',views.UserapiViewId),
    path('articles',views.ArticlesView),
    path('articles/<int:id>',views.ArticlesViewId),
    path('categories',views.CategoriesView),
    path('categories/<int:id>',views.CategoriesViewID),
    path('categories/<int:id>/children',views.CategoriesViewChilden),
    path('categories/<int:id>/ancestors',views.CategoriesViewParent),
]