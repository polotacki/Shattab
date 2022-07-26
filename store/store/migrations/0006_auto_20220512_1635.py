# Generated by Django 3.0.5 on 2022-05-12 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20220512_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='emailAddress',
        ),
        migrations.RemoveField(
            model_name='services',
            name='name',
        ),
        migrations.AddField(
            model_name='services',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Customer'),
        ),
    ]