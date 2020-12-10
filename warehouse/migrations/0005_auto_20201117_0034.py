# Generated by Django 3.1.2 on 2020-11-16 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0004_warehouse'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='address',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
