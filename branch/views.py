from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from warehouse . models import Supplier,ProductModel
# Create your views here.

def warehouse_login(request):
    if request.method == 'POST':
        username  = request.POST['username']
        password = request.POST['password']
        #check user entred username and password
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return render(request, 'branch/dashboard.html')
        else:
            messages.error(request, ' Wrong username/password!')
            return redirect('branch_login')
    else:    
        return render(request, 'branch/login.html' )

def logoutuser(request):
    auth.logout(request)
    return redirect('branch_login')
