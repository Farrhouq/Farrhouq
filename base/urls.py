from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login', views.loginUser, name='login'),
    path('home_page', views.home_page, name='home'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('update/<str:pk>', views.update_item, name='update'),
    path('logoutUser', views.logoutUser, name='logoutUser')
]

