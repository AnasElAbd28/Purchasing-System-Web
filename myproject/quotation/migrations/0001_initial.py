# Generated by Django 4.1.4 on 2023-01-11 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='quotation',
            fields=[
                ('Quotation_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Quotation_Number', models.CharField(max_length=15, null=True)),
                ('Valid_Date', models.DateField(max_length=6)),
                ('Creation_Date', models.DateTimeField(null=True)),
                ('status', models.BooleanField(default=False)),
                ('seller_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.seller')),
            ],
        ),
        migrations.CreateModel(
            name='QuotationProduct',
            fields=[
                ('Product_ID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=20)),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length=60)),
                ('proposed_quantity', models.IntegerField()),
                ('selected_quantity', models.IntegerField(null=True)),
                ('Total_Price', models.IntegerField()),
                ('quottion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotation.quotation')),
            ],
        ),
    ]
