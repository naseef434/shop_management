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
