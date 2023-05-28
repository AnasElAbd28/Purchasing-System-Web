# Generated by Django 4.1.5 on 2023-01-23 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('Manager_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Manager_fname', models.TextField(max_length=20)),
                ('Manager_lname', models.TextField(max_length=30)),
                ('Manager_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('Finance_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Finance_fname', models.TextField(max_length=20)),
                ('Finance_lname', models.TextField(max_length=30)),
                ('Finance_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
