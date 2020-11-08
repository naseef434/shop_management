from django.db import models

#supplier Model
class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    supplier_address = models.CharField(max_length=300)
    supplier_phone = models.CharField(max_length=12)
    gst_uin  = models.CharField(max_length=30)
    state_name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    brand_name = models.CharField(max_length=50)

#Branch Model
class Branch(models.Model):
    branch_name = models.CharField(max_length=50)
    discription = models.CharField(max_length=50, default=None)

#product model
class ProductModel(models.Model):
    name  = models.CharField(max_length=50, null=False)
    brand = models.ForeignKey(Supplier,on_delete=models.CASCADE)

class Variants(models.Model):
    color = models.CharField(max_length=60)
    ram = models.CharField(max_length=40)
    rom = models.CharField(max_length=60)
    brand = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

