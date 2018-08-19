from myshop.forms import *
from myshop.models import *
from django.shortcuts import render,redirect


def display_products(request):
     objects=Product.objects.all()
     return render(request,'displayproduct.html',{"objects":objects})

def add_product(request):
    form=ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('productslist')
    return render(request,'addproduct.html',{"form":form})
      
def update_product(request,value):
    object=Product.objects.get(id=value)
    form=ProductForm(request.POST or None, instance = object)
    if form.is_valid():
        form.save()
        return redirect('productslist')
    return render(request, 'addproduct.html',{"form":form, "product":object})

def delete_product(request,id):
    product=Product.objects.get(pk=id)
    if request.method=='POST':
        product.delete()
        return redirect('productslist')
    return render (request,'confirmdelete.html',{"product":product})

    




