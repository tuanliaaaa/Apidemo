from unicodedata import name
from django.urls import path
from .loginViews import Login
from .homeViews import Home
from .signupViews import Signup
from Category.views import Category
urlpatterns = [
    path('login/',Login.as_view(),name="Login"),
    path('home',Home.as_view(),name="Home"),
    path('signup/',Signup.as_view(),name="Signup"),
    path('Category/',Category.as_view(),name="Category"),
]