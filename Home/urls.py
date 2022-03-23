from django.urls import path
from apidemo.loginViews import LoginAjax
urlpatterns = [
    path('',LoginAjax.as_view()),
]