from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

from warehouse . models import Supplier,Branch,ProductModel,Variants


def warehouse_login(request):
    if request.method == "GET":
        return render(request, 'warehouse/login.html')

    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']  
        
        if username == "admin" and password == "admin":
            request.session['username'] = username
            return render(request, 'warehouse/dashboard.html')

def dashboard(request):
    if request.session.has_key('username'):
        return render(request, 'warehouse/dashboard.html')
    else:
        return redirect(warehouse_login)
def supplier(request):
    suppliers = Supplier.objects.all()
    return render(request, 'warehouse/supplier_list.html',{'suppliers':suppliers})


#supplier management start here
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
        return redirect('supplier')
    
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
        return redirect('supplier')

def delete_supplier(request, id):
    supplier = Supplier.objects.get(id=id)  
    supplier.delete()  
    messages.info(request,"Supplier Deleted Successfully")
    return redirect('supplier')

#end supplier management


#branch management start here

def branch(request):
    branches = Branch.objects.all()
    return render(request, 'warehouse/branch_list.html',{'branches':branches})

def add_branch(request):
    if request.method == "GET":
        return render(request, 'warehouse/add_branch.html')
    elif request.method == "POST":
        branch = Branch()
        branch.branch_name = request.POST['branch_name']
        branch.discription = request.POST['discription']
        branch.save()
        messages.success(request, 'Branch Added successfully')
        return redirect('branch')

def edit_branch(request, id):
    branch = Branch.objects.get(id=id)
    return render(request, 'warehouse/edit_branch.html',{'branch':branch})

def update_branch(request, id):
    if request.method == "POST":
        branch  = Branch.objects.get(id=id)
        branch.branch_name = request.POST['branch_name']
        branch.discription = request.POST['discription']
        branch.save()
        messages.info(request, 'Branch Updated Successfully! ')
        return redirect('branch')

def delete_branch(request, id):
    branch = Branch.objects.get(id=id)  
    branch.delete()  
    messages.info(request,"Branch Deleted Successfully")
    return redirect('branch')
#end branch management


#product managemnt

def product(request):
    products = ProductModel.objects.all()
    return render(request, 'warehouse/product_list.html',{'products':products})

def add_product(request):
    if request.method == "GET":
        brands = Supplier.objects.all()
        return render(request, 'warehouse/add_product.html',{'brands':brands})
    elif request.method == "POST":
        product = ProductModel()
        product.name = request.POST['product_name']
        product.brand_id = request.POST['brand']
        product.save()
        messages.success(request, 'Product added succesfully!')
        return redirect('product')
    else:
        return HttpResponse("something goes wrong")

def edit_product(request, id):
    product = ProductModel.objects.get(id=id)
    brands  = Supplier.objects.all()
    return render(request, 'warehouse/edit_product.html', {'product':product, 'brands':brands})

def update_product(request, id):
    if request.method == "POST":
        product  = ProductModel.objects.get(id=id)
        product = ProductModel()
        product.name = request.POST['product_name']
        product.brand_id = request.POST['brand']
        product.save()
        messages.success(request, 'Product Upadated succesfully!')
        return redirect('product')

def delete_product(request, id):
    product = ProductModel.objects.get(id=id)  
    product.delete()  
    messages.info(request,"Product Deleted Successfully")
    return redirect('product')
#product management end here

#variants managing

def variants(request):
    variants = Variants.objects.all()
    return render(request, 'warehouse/variants.html',{'variants':variants})

def add_variants(request):
    if request.method == "GET":
        brands  = Supplier.objects.all()
        products = ProductModel.objects.all()
        return render(request, 'warehouse/add_variants.html',{'products':products, 'brands':brands})
    elif request.method == "POST":
        variants = Variants()
        variants.color = request.POST['product_color']
        variants.ram = request.POST['ram']
        variants.rom = request.POST['rom']
        variants.brand = request.POST['brand']
        variants.product = request.POST['product']
        variants.save()
        messages.success(request, 'Variants Added succesfully!')
        return redirect('variants')

def admin_logout(request):
    request.session.flush()
    return render(request, 'warehouse/login.html')