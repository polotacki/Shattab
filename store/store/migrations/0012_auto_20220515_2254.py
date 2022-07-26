# Generated by Django 3.0.5 on 2022-05-15 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0011_auto_20220513_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='services',
            name='ApartmentMeters',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='services',
            name='Budget',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='services',
            name='NumberOfRooms',
            field=models.CharField(max_length=200),
        ),
    ]
