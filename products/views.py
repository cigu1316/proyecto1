from django.http import HttpResponse
from django.shortcuts import render

from products.models import Products,Category
from products.forms import ProductsForm

def create_product(request):
    if request.method == 'GET':
        context ={
            'form': ProductsForm()
        }
        return render(request,'products/create_product.html', context=context)  
      
    elif request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            Products.objects.create(
                name = form.cleaned_data['name'],
                price =form.cleaned_data['price'],
                stock =form.cleaned_data['stock'],
        )
            context={ 
                'messaje':'producto creado exitosamente'
            }
        return render (request,'products/create_product.html', context=context)
            
    else:
        context = {
            'form_errors' : form.errors,
            'form': ProductsForm()
        }
        return render (request,'products/create_product.html', context={})
            

def list_products(request):
    if 'search' in request.GET:
        search = request.GET['search']
        products= Products.objects.filter(name__contains=search)
    else:
        products = Products.objects.all()
    context = {
        'products': products,
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