from unicodedata import name
from django.urls import path
from .loginViews import Login
from .homeViews import Home
from .signupViews import Signup
urlpatterns = [
    path('login/',Login.as_view(),name="Login"),
    path('home',Home.as_view()),
    path('signup/',Signup.as_view()),
]