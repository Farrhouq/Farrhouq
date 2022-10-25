from django.urls import path
from . import views

urlpatterns = [
    path("", views.register, name="register"),
    path("login/", views.loginUser, name="login"),
    path("home", views.home_page, name="home"),
    path("delete/<str:pk>", views.delete, name="delete"),
    path("logoutUser", views.logoutUser, name="logoutUser"),
    path("done/<str:pk>", views.done, name="done"),
]
