from django.urls import path
from . import views
urlpatterns = [
    path('', views.warehouse_login, name='branch_login'),
    path('', views.logoutuser, name='logoutuser'),
]