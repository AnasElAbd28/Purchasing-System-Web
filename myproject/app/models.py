from django.db import models

from django.contrib.auth.models import User

class Seller(models.Model):
    seller_id = models.AutoField(primary_key=True)
    seller_user = models.OneToOneField(User, on_delete=models.CASCADE)
    seller_name = models.CharField(null=True, max_length= 30)
    seller_email = models.EmailField(null=True)
    seller_address = models.TextField(max_length=100)
    seller_phone = models.PositiveIntegerField()

    def __str__(self):  
        return str(self.seller_id)
    
class Staff(models.Model):
    Staff_ID = models.AutoField(primary_key=True)
    Staff_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    Staff_fname = models.TextField(max_length=20)
    Staff_lname = models.TextField(max_length=20)
    Staff_department = models.TextField(max_length=30)
    def __str__(self):
        return str(self.Staff_ID)

class Finance(models.Model):
    Finance_ID = models.AutoField(primary_key=True)
    Finance_user = models.OneToOneField(User, on_delete=models.CASCADE)
    Finance_fname = models.TextField(max_length=20)
    Finance_lname = models.TextField(max_length=30)

    def __str__(self):
        return str(self.Finance_ID)


class Manager(models.Model):
    Manager_ID = models.AutoField(primary_key=True)
    Manager_user = models.OneToOneField(User, on_delete=models.CASCADE)
    Manager_fname = models.TextField(max_length=20)
    Manager_lname = models.TextField(max_length=30)

    def __str__(self):
        return str(self.Manager_ID)