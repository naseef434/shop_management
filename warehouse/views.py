from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from warehouse . models import Supplier,ProductModel,Warehouse


def warehouse_login(request):
    if request.session.has_key('username'):
        return redirect('dashboard')
  
    elif request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']  
            if username == "admin" and password == "admin":
                request.session['username'] = username
                return render(request, 'warehouse/dashboard.html')
            else:
                messages.error(request, ' Wrong username/password!')
                return render(request, 'warehouse/login.html')
    return render(request, 'warehouse/login.html')

def dashboard(request):
    if request.session.has_key('username'):
        return render(request, 'warehouse/dashboard.html')
    else:
        return redirect('login')

#supplier management start here
def supplier(request):
    if request.session.has_key('username'):
        suppliers = Supplier.objects.all()
        return render(request, 'warehouse/supplier_list.html',{'suppliers':suppliers})
    else:
        return redirect('login')
    


def add_supplier(request):
     if request.session.has_key('username'):
         if request.method == "POST": 
            try:
                name = request.POST['name']
                brand = request.POST['brand']
                phone = request.POST['phone']
                gst = request.POST['gst']
                state = request.POST['state']
                code = request.POST['code']
                email = request.POST['email']
                address = request.POST['address']
                if Supplier.objects.filter(supplier_name=name, brand_name=brand).exists():
                    messages.success(request, 'Supplier already Exist')
                    return redirect('supplier')
                else:
                    supplier  = Supplier()
                    supplier.supplier_name = name
                    supplier.brand_name = brand
                    supplier.supplier_phone = phone
                    supplier.gst_uin  = gst
                    supplier.state_name = state
                    supplier.code = code
                    supplier.email = email
                    supplier.supplier_address =address
                    supplier.save()
                    messages.success(request, 'Supplier Added successfully')
                    return redirect('supplier')    
            except:
                messages.success(request, 'Something Went Wrong')
                return redirect('add_supplier')
         else:
            return render(request, 'warehouse/add_supplier.html')
     else:
         return redirect('login')

def edit_supplier(request, id):
    if request.session.has_key('username'):
        supplier = Supplier.objects.get(id=id)
        return render(request, 'warehouse/edit_supplier.html', {'supplier':supplier})
    else:
         return redirect('login')
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
    if request.session.has_key('username'):
        branches = User.objects.all()
        return render(request, 'warehouse/branch_list.html',{'branches':branches})
    else:
        return redirect('login')


def add_branch(request):
    if request.method == "GET":
        return render(request, 'warehouse/add_branch.html')
    elif request.method == "POST":
        first_name = request.POST['branch_name']
        last_name = request.POST['discription']
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password)
        user.save()
        messages.success(request, 'Branch Added successfully')
        return redirect('branch')

def edit_branch(request, id):
    branch = User.objects.get(id=id)
    return render(request, 'warehouse/edit_branch.html',{'branch':branch})

def update_branch(request, id):
    if request.method == "POST":
        branch  = User.objects.get(id=id)
        branch.branch_name = request.POST['branch_name']
        branch.discription = request.POST['discription']
        branch.save()
        messages.info(request, 'Branch Updated Successfully! ')
        return redirect('branch')

def delete_branch(request, id):
    branch = User.objects.get(id=id)  
    branch.delete()  
    messages.info(request,"Branch Deleted Successfully")
    return redirect('branch')
#end branch management


#product managemnt

def product(request):
    if request.session.has_key('username'):
        products = ProductModel.objects.all()
        return render(request, 'warehouse/product_list.html',{'products':products})
    else:
        return redirect('login')

def add_product(request):
    if request.method == "GET":
        brands = Supplier.objects.all()
        return render(request, 'warehouse/add_product.html',{'brands':brands})
    elif request.method == "POST":
        product = ProductModel()
        product.name = request.POST['product_name']
        product.brand_id = request.POST['brand']
        product.color = request.POST['color']
        product.ram = request.POST['ram']
        product.rom = request.POST['rom']
        product.discription = request.POST['discription']
        product.save()
        messages.success(request, 'Product added succesfully!')
        return redirect('product')
    else:
        return HttpResponse("something goes wrong")

def edit_product(request, id):
    if request.session.has_key('username'): 
        product = ProductModel.objects.get(id=id)
        brands  = Supplier.objects.all()
        return render(request, 'warehouse/edit_product.html', {'product':product, 'brands':brands})
    else:
        return redirect('login')

def update_product(request, id):
    if request.method == "POST":
        product  = ProductModel.objects.get(id=id)
        product.name = request.POST['product_name']
        product.brand_id = request.POST['brand']
        product.color = request.POST['color']
        product.ram = request.POST['ram']
        product.rom = request.POST['rom']
        product.discription = request.POST['discription']
        product.save()
        messages.success(request, 'Product Upadated succesfully!')
        return redirect('product')

def delete_product(request, id):
    product = ProductModel.objects.get(id=id)  
    product.delete()  
    messages.info(request,"Product Deleted Successfully")
    return redirect('product')
#product management end here
def purchase(request):
    return render(request, 'warehouse/purchase.html')

def add_purchase(request):
    supplier = Supplier.objects.all()
    product  = ProductModel.objects.all()
    return render(request, 'warehouse/add_purchase.html',{'suppliers':supplier,'products':product})


def purchase_invoice(request):
    return render(request, 'warehouse/purchase_invoice.html')

def settings(request):
    info = Warehouse.objects.get(id=1)
    print(info)
    return render(request, 'warehouse/settings.html',{'info':info})    

def ware_house(request):
    if request.method == "POST":
        warehouse = Warehouse()
        warehouse.name = request.POST['warehouse_name']
        warehouse.phone = request.POST['phone']
        warehouse.gst = request.POST['gst']
        warehouse.email = request.POST['email']
        warehouse.state = request.POST['state']
        warehouse.code = request.POST['code']
        warehouse.address = request.POST['address']
        warehouse.save()
        messages.success(request, 'Warehouse Created Successfully')
        return redirect('dashboard')

    return render(request, 'warehouse/ware_house.html')



def admin_logout(request):
    if request.session.has_key('username'):
        request.session.delete()
        return redirect('login')
    else:
        return redirect('login')

