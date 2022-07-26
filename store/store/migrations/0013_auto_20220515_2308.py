# Generated by Django 3.0.5 on 2022-05-15 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20220515_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='customer',
        ),
        migrations.AddField(
            model_name='services',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
