from typing import ValuesView
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('', views.loginUser, name='login'),
    path('home_page', views.home_page, name='home'),
    path('delete/<str:pk>', views.delete_item, name='delete'),
    path('update/<str:pk>', views.update_item, name='update'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('deleteRoom/<str:pk>', views.deleteRoom, name='deleteRoom'),
    path('room/<str:pk>', views.room, name='room'),
    path('deleteRoomItem/<str:pk>', views.deleteRoomItem, name='deleteRoomItem'),
    path('createItem/<str:pk>', views.addItem, name='createItem'),
    path('change/<str:pk>', views.change, name='change'),
    path('custom', views.add, name='custom'),
    path('make_priority/<str:pk>', views.make_priority, name='make_priority'),
]

