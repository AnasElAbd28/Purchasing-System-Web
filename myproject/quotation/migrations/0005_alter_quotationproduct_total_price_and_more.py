# Generated by Django 4.1.4 on 2023-01-18 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0004_alter_quotation_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotationproduct',
            name='Total_Price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quotationproduct',
            name='price',
            field=models.FloatField(),
        ),
    ]
