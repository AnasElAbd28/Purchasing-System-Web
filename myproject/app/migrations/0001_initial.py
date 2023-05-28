# Generated by Django 4.1.4 on 2023-01-11 01:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('Staff_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Staff_fname', models.TextField(max_length=20)),
                ('Staff_lname', models.TextField(max_length=20)),
                ('Staff_department', models.TextField(max_length=30)),
                ('Staff_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('seller_id', models.AutoField(primary_key=True, serialize=False)),
                ('seller_name', models.CharField(max_length=30, null=True)),
                ('seller_email', models.EmailField(max_length=254, null=True)),
                ('seller_address', models.TextField(max_length=100)),
                ('seller_phone', models.PositiveIntegerField()),
                ('seller_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
