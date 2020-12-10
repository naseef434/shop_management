from django.urls import path
from . import views
from branch.views import TestView
urlpatterns = [
    path('', views.warehouse_login, name='branch_login'),
    path('user_dashboard', views.dashboard, name="user_dashboard"),
    path('logout_user', views.logoutuser, name='logoutuser'),
    path('hello-world', TestView.as_view(), name='hello_world'),
]