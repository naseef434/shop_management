from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

from warehouse . models import Supplier

def warehouse_login(request):
    return render(request, 'warehouse/login.html')

def dashboard(request):
     return render(request, 'warehouse/dashboard.html')

def supplier(request):
    return render(request, 'warehouse/supplier_list.html')

def add_supplier(request):
    if request.method == "POST":
        supplier  = Supplier()
        supplier.supplier_name = request.POST.get('supplier_name') 
        supplier.brand_name  = request.POST.get('brand')
        supplier.supplier_phone  = request.POST.get('phone')
        supplier.gst_uin  = request.POST.get('gst')
        supplier.state_name  = request.POST.get('state')
        supplier.code  = request.POST.get('code')
        supplier.email  = request.POST.get('email')
        supplier.supplier_address  = request.POST.get('address')
        supplier.save()
        messages.success(request, 'Supplier Added successfully')
        return render(request, 'warehouse/supplier_list.html')
    
    
