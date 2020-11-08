# Generated by Django 3.1.2 on 2020-11-08 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0005_auto_20201108_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='brand_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='code',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='state_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='supplier_address',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='supplier_name',
            field=models.CharField(max_length=100),
        ),
    ]
