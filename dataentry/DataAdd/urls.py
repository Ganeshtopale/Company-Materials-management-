# DataAdd/urls.py

'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all-products/', views.all_products, name='all_products'),
    path('product/add/', views.add_product, name='product_add'),
    path('product/edit/<int:pk>/', views.edit_product, name='product_edit'),
    path('product/delete/<int:pk>/', views.delete_product, name='product_delete'),
    path('product/pdf/<int:pk>/', views.generate_pdf, name='product_pdf'),
]
'''

# DataAdd/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_product, name='product_add'),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('pdf/<int:pk>/', views.generate_pdf, name='generate_pdf'),
    path('all-products/', views.all_products, name='all_products'),
]
