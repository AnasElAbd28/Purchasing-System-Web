# Generated by Django 4.1.5 on 2023-01-25 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchaseOrder', '0004_alter_purchaseorder_seller_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='Seller_Name',
            field=models.TextField(max_length=30),
        ),
    ]
