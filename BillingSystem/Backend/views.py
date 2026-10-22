from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

class ProductsView(APIView):
    
    def get(self,request):
        all_products = Products.objects.all()
        
        products_data = []
        
        for product in all_products:
            single_product = {
                "product_name": product.product_name,
                "price": product.price,
                "code": product.code
            }       
            products_data.append(single_product)
        
        return Response(products_data)
    
    
    
    def post(self,request):
        new_product = Products(
            product_name=request.data.get("product_name"),
            code=request.data.get("code"),
            price=request.data.get("price"))
        new_product.save()
        
        return Response("Product Added Successfully")
    
class ProductDetailView(APIView):
    def get(self,request,id):
        product = Products.objects.get(id=id)
        
        single_product={
                               "product_name": product.product_name,
                               "price": product.price,
                               "code": product.code
                            }       
        return Response(single_product)
    
    
    def patch(self,request,id):
        product = Products.objects.filter(id=id)
        print(request.data)
        
        product.update(
            product_name=request.data.get("product_name"),
            code=request.data.get("code"),
            price=request.data.get("price"))
        
        return Response("Product Updated Successfully")  
    
    
    def delete(self,request,id):
        product = Products.objects.get(id=id)
        product.delete()
        
        return Response("Product Deleted Successfully")   
  