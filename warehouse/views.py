from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

from warehouse . models import Supplier

def warehouse_login(request):
    return render(request, 'warehouse/login.html')

def dashboard(request):
     return render(request, 'warehouse/dashboard.html')

def supplier(request):
    suppliers = Supplier.objects.all()
    return render(request, 'warehouse/supplier_list.html',{'suppliers':suppliers})



def add_supplier(request):
    if request.method == "GET":
        return render(request, 'warehouse/add_supplier.html')
    elif request.method == "POST":
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
        return redirect('/supplier')
    
def edit_supplier(request, id):
    supplier = Supplier.objects.get(id=id)
    return render(request, 'warehouse/edit_supplier.html', {'supplier':supplier})

def update_supplier(request, id):
    if request.method == "POST":
        supplier = Supplier.objects.get(id=id)
        supplier.supplier_name = request.POST.get('supplier_name') 
        supplier.brand_name  = request.POST.get('brand')
        supplier.supplier_phone  = request.POST.get('phone')
        supplier.gst_uin  = request.POST.get('gst')
        supplier.state_name  = request.POST.get('state')
        supplier.code  = request.POST.get('code')
        supplier.email  = request.POST.get('email')
        supplier.supplier_address  = request.POST.get('address')
        supplier.save()
        messages.warning(request, 'Supplier Updated successfully')
        return redirect('/supplier')

def delete_supplier(request, id):
    supplier = Supplier.objects.get(id=id)  
    supplier.delete()  
    messages.info(request,"Supplier Deleted Successfully")
    return redirect('/supplier')