from . models import *
from django import forms

class ProductForm(forms.ModelForm):
    prd_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control" ,"placeholder":"Enter Product name"}))
    prd_description=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control" ,"placeholder":"describe "}))
    prd_size=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control" ,"placeholder":"L/S/L/XL/XXL"}))
    prd_price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control" ,"placeholder":"price"}))
    prd_pic=forms.FileField(widget=forms.FileInput(attrs={"class":"form-control" ,"placeholder":"select image"}))
    
    
    class Meta:
        model=Product
        fields=[
                'prd_name',
                'prd_description',
                'prd_size',
                'prd_price',
                'prd_pic'
               ]


class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=[
                'cst_name',
                'cst_contact',
                'cst_email',
                'cst_address'
               ]

class SupplierForm(forms.ModelForm):
    class Meta:
        model=Supplier
        fields=[
                'sup_name',
                'sup_contact',
                'sup_email',
                'sup_address'
               ]

class OrderForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields=[
                'ord_product',
                'ord_transactionnumber',
                
               ]

class ShipmentForm(forms.ModelForm):
    class Meta:
        model=Shipment
        fields=[
                'shp_curreir',
                'shp_departure_date',
                'shp_delivery_date',
                'shp_cost',
                 'customer'
                ]


