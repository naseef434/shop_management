from django.urls import path
from . import views

urlpatterns = [
    path('', views.warehouse_login, name='login'),
    path('dashboard', views.dashboard),
    
    path('supplier', views.supplier,name='supplier'),
    path('add_supplier', views.add_supplier),
    path('edit_supplier/<int:id>', views.edit_supplier),  
    path('update_supplier/<int:id>', views.update_supplier), 
    path('delete_supplier/<int:id>/', views.delete_supplier), 
    
    path('branch', views.branch, name='branch'),
    path('add_branch', views.add_branch),
    path('edit_branch/<int:id>', views.edit_branch,name="edit_branch"),
    path('update_branch/<int:id>', views.update_branch),
    path('delete_branch/<int:id>', views.delete_branch,name='delete_branch'), 
    
    path('product', views.product, name='product'),
    path('add_product', views.add_product, name='add_product'),
    path('edit_product/<int:id>', views.edit_product),
    path('update_product/<int:id>', views.update_product),
    path('delete_product/<int:id>', views.delete_product,name='delete_product'),

    path('variants', views.variants, name='variants'),
    path('add_variants', views.add_variants, name='add_variants'),
    path('edit_product/<int:id>', views.edit_product),
    path('update_product/<int:id>', views.update_product),
    path('delete_product/<int:id>', views.delete_product,name='delete_product'),

    path('logout', views.admin_logout, name='logout'),
]