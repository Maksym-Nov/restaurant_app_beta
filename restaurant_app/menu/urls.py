from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('<int:id>/', views.dish_detail, name='dish_detail'),
]
