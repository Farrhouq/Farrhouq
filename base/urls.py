from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('update/<str:pk>', views.update_item, name='update'),
]

