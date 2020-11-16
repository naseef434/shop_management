# Generated by Django 3.1.2 on 2020-11-15 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=50)),
                ('discription', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=100)),
                ('supplier_address', models.CharField(max_length=300)),
                ('supplier_phone', models.CharField(max_length=12)),
                ('gst_uin', models.CharField(max_length=30)),
                ('state_name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('brand_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.supplier')),
            ],
        ),
    ]
