# Generated by Django 4.1.4 on 2023-01-13 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0002_rename_quottion_id_quotationproduct_quotation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='Valid_Date',
            field=models.DateField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='quotationproduct',
            name='selected_quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]