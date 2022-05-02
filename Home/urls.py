from unicodedata import name
from django.urls import path
from .loginViews import Login
from .homeViews import Home
from .signupViews import Signup
from Category.views import Category
urlpatterns = [
    path('login/',Login.as_view(),name="Login"),
    path('home',Home.as_view()),
    path('signup/',Signup.as_view()),
    path('Category/',Category.as_view()),
]