from django.db import models
from django.contrib.auth.models import User
from app.models import Finance 
from decimal import Decimal

# Create your models here.

#Iskanth and Emad
class purchaseOrder(models.Model):
    PO_ID = models.AutoField(primary_key=True)
    Purchaseorder_Number = models.CharField(max_length=15, null=True)
    Valid_Date = models.DateField(max_length=6,null=True)
    Creation_Date = models.DateTimeField(auto_now_add=True,null = True)
    status = models.BooleanField(default=False)
    finance_ID = models.ForeignKey(Finance, on_delete=models.CASCADE, null=True)
    Seller_Name = models.TextField(max_length= 30)
    Seller_Address = models.TextField(max_length= 100)
    Quotation_Number = models.CharField(max_length=15, null=True)
    

    def __str__(self):
        return str(self.PO_ID)

class PurchaseOrderProduct(models.Model):
    Product_ID = models.AutoField(primary_key=True)
    name = models.TextField(max_length=20)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    description = models.TextField(max_length= 60)
    proposed_quantity = models.IntegerField(null=False)
    selected_quantity = models.IntegerField(blank=True, null=True)
    Total_Price = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    purchaseorder_id = models.ForeignKey(purchaseOrder, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.Product_ID)