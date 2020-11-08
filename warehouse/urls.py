from django.urls import path
from . import views

urlpatterns = [
    path('', views.warehouse_login),
    path('dashboard', views.dashboard),
    path('supplier', views.supplier,name='supplier'),
    path('add_supplier', views.add_supplier),
    path('edit_supplier/<int:id>', views.edit_supplier),  
    path('update_supplier/<int:id>', views.update_supplier), 
    path('delete_supplier/<int:id>', views.delete_supplier), 
    
]