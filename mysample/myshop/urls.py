from django.urls import path
from myshop.Views import Product_View,customerview



urlpatterns=[
        path('', Product_View.display_products, name='productslist'),
        path('addproduct/', Product_View.add_product, name='addproduct'),
        path('updateproduct/<int:value>/',Product_View.update_product, name='updateproduct'),
        path('deleteproduct/<int:id>/',Product_View.delete_product, name='deleteproduct'),
             ]
