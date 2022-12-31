from django.http import HttpResponse
from django.shortcuts import render

from products.models import Products,Category

def create_product(request):
    new_product=Products.objects.create(name ='Coca Cola 1 litro', price = 300 , stock = False)
    print(new_product)
    return HttpResponse('nuevo producto creado')

def list_products(request):
    all_products = Products.objects.all
    print(all_products)
    context = {
        'products': all_products,
        
    }
    return render(request,'products/list_products.html',context=context)

def list_categories(request):
    all_categories = Category.objects.all()
    context = {
        'categories': all_categories,
     }
    return render(request,'products/list_categories.html',context=context)

def create_category(request,name):
    new_category = Category.objects.create(name=name)
    print(new_category)
    return HttpResponse('nuevo categoria creada')