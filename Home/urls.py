from unicodedata import name
from django.urls import path
from apidemo.loginViews import LoginAjax
from .homeViews import Home
urlpatterns = [
    path('login/',LoginAjax.as_view(),name="Login"),
    path('home',Home.as_view()),
]