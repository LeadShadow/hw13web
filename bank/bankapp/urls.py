from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path("signup", views.signup, name='signup'),
    path("loginuser", views.loginuser, name='loginuser'),
    path("logoutuser", views.logoutuser, name='logoutuser'),
    path("savings", views.savings, name='savings'),
]
