# Generated by Django 2.1 on 2018-08-17 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cst_name', models.CharField(max_length=25)),
                ('cst_contact', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('cst_address', models.TextField(max_length=100)),
                ('cst_email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ord_date', models.DateField(auto_now=True)),
                ('ord_transactionnumber', models.PositiveIntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.ProtectedError, to='myshop.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prd_name', models.CharField(max_length=25)),
                ('prd_description', models.CharField(max_length=80)),
                ('prd_size', models.CharField(max_length=3)),
                ('prd_price', models.PositiveIntegerField()),
                ('prd_pic', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shp_curreir', models.CharField(max_length=25)),
                ('shp_departure_date', models.DateField()),
                ('shp_delivery_date', models.DateField()),
                ('shp_cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.ProtectedError, to='myshop.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.ProtectedError, to='myshop.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('sup_name', models.CharField(max_length=25)),
                ('sup_contact', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('sup_address', models.TextField(max_length=100)),
                ('sup_email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.ProtectedError, to='myshop.Product')),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='ord_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.ProtectedError, to='myshop.Product'),
        ),
    ]
