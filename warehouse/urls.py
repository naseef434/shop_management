from django.urls import path
from . import views

urlpatterns = [
    path('', views.warehouse_login),
    path('dashboard', views.dashboard),
    path('supplier', views.supplier),
    path('add_supplier', views.add_supplier),
    
]