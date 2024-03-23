from django.urls import path
from . import views

urlpatterns = [
    path('', views.topic_list, name='tajriba'),
    path('users/', views.user_list , name='user_list'),
    path('jadval/', views.table_list, name='table_list'),

    path('item/', views.item_list, name='item_list'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('create/', views.item_create, name='item_create'),
    path('item/<int:pk>/update/', views.item_update, name='item_update'),
    path('item/<int:pk>/delete/', views.item_delete, name='item_delete'),

]
