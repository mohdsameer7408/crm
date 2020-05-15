from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product, name='products'),
    path('customer/<str:pk>/', views.customers, name='customer'),
    path('create-order/<str:pk>/', views.create_order, name='create_order'),
    path('update-order/<str:pk>/', views.update_order, name='update_order'),
    path('delete-order/<str:pk>/', views.delete_order, name='delete_order')
]
