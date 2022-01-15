from django.urls import path, include
from .views import ProductCreate, all_Product


urlpatterns = [
    path('',ProductCreate , name='product'),
    path('all/',all_Product , name='allpro'),


]
