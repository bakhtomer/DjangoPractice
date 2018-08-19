"""
Conventions for this project is :
Class names startwithCapital letter and follow camel rule
method seperated by underscore and lower cased
variables of class are first 3 ltr of class name under score veriable all lower cased
"""

from django.db import models

class Product(models.Model):
    prd_name=models.CharField(max_length=25)
    prd_description=models.CharField(max_length=80)
    prd_size=models.CharField(max_length=3)
    prd_price=models.PositiveIntegerField()
    prd_pic=models.ImageField(blank=True)

    def __str__(self):
        return f" name:{self.prd_name}contact:  {self.prd_description} address:  {self.prd_size}email: {self.prd_price},{self.prd_pic}"



class Customer(models.Model):
    cst_name=models.CharField(max_length=25)
    cst_contact= models.IntegerField(unique=True,primary_key=True)
    cst_address= models.TextField(max_length=100)
    cst_email=models.EmailField(blank=True,null=True,unique=True)

    def __str__(self):
        return f" name:  {self.cst_name}\ncontact:  {self.cst_contact}\n address:  {self.cst_address}\n email: {self.cst_email}"


class Supplier(models.Model):
    sup_name=models.CharField(max_length=25)
    sup_contact= models.IntegerField(unique=True,primary_key=True)
    sup_address= models.TextField(max_length=100)
    sup_email=models.EmailField(blank=True,null=True,unique=True)
    product=models.ForeignKey(Product,on_delete=models.ProtectedError)

    def __str__(self):
        return "%s %d %s %s %d"%sup_name%sup_contact%sup_address%sup_email%porduct
    

class Shipment(models.Model):
    shp_curreir= models.CharField(max_length=25)
    shp_departure_date= models.DateField()
    shp_delivery_date=models.DateField()
    shp_cost=models.DecimalField(max_digits=5,decimal_places=2)
    product=models.ForeignKey(Product,on_delete=models.ProtectedError) 
    customer= models.ForeignKey(Customer,on_delete=models.ProtectedError)

    def __str__(self):
        return "{} {} {} {} ".format(shp_curreir, shp_departure_date, shp_delivery_date, shp_cost)

class Orders(models.Model):
      
    ord_product=models.ForeignKey(Product,on_delete=models.ProtectedError)
    ord_date=models.DateField(auto_now=True)
    customer=models.ForeignKey(Customer,on_delete=models.ProtectedError)
    ord_transactionnumber=models.PositiveIntegerField()
   
    def __str__(self):
        return "{} {} {} {} ".format(ord_product, ord_date,ord_transuctionnumber, customer)

    # Create your models here.
