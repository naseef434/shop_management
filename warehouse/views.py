from django.shortcuts import render,redirect
from django.http import HttpResponse


def warehouse_login(request):
    return render(request, 'warehouse/login.html')