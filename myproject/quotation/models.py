from django.db import models
from django.contrib.auth.models import User
from app.models import Seller
from decimal import Decimal

# Create your models here.


class quotation(models.Model):
    Quotation_ID = models.AutoField(primary_key=True)
    Quotation_Number = models.CharField(max_length=15, null=True)
    Valid_Date = models.DateField(max_length=6,null=True)
    Creation_Date = models.DateTimeField(auto_now_add=True,null = True)
    status = models.BooleanField(default=False)
    seller_ID = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return str(self.Quotation_ID)

class QuotationProduct(models.Model):
    Product_ID = models.AutoField(primary_key=True)
    name = models.TextField(max_length=20)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    description = models.TextField(max_length= 60)
    proposed_quantity = models.IntegerField(null=False)
    selected_quantity = models.IntegerField(blank=True, null=True)
    Total_Price = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    quotation_id = models.ForeignKey(quotation, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.Product_ID)

    