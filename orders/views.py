from django.shortcuts import render
from orders.models import Orders
from django.http import HttpResponse


def list_orders(requets):
    orders = Orders.objects.all()
    context = {
        'orders': orders ,
    }
    return render (requets,'orders/list_orders.html',context=context)

def create_orders(request):
    new_orders=Orders.objects.create(client ='gustavo cicerchia', product = 'cerbeza' , payment_method = 'cash')
    return HttpResponse('nueva orden creada')    