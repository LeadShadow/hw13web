from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path("signup", views.signup, name='signup'),
    path("loginuser", views.loginuser, name='loginuser'),
    path("logoutuser", views.logoutuser, name='logoutuser'),
    path("add_savings", views.add_savings, name='add_savings'),
    path("show_savings", views.show_savings, name='show_savings'),
]
