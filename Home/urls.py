from unicodedata import name
from django.urls import path
from .loginViews import Login
from .homeViews import Home
urlpatterns = [
    path('login/',Login.as_view(),name="Login"),
    path('home',Home.as_view()),
]