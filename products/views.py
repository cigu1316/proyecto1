from django.http import HttpResponse
from django.shortcuts import render

from products.models import Products

def create_product(request):
    new_product=Products.objects.create(name ='Coca Cola 500 ml', price = 200 , stock = True)
    print(new_product)
    return HttpResponse('nuevo producto creado')

def list_products(request):
    all_products =Products.objects.all
    print(all_products)
    context = {
        'products': all_products,
        
    }
    return render(request,'list_products.html',context=context)