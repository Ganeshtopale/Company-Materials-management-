from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_product/', views.add_product, name='add_product'),
    path('update_product/<int:pk>/', views.update_product, name='update_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    path('export_to_excel/', views.export_to_excel, name='export_to_excel'),
    path('generate_pdf/<int:pk>/', views.generate_pdf, name='generate_pdf'),
]
