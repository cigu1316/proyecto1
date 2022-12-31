from django.contrib import admin
from django.urls import path , include
from orders.views import list_orders,create_orders
                            
urlpatterns = [
     path('list-orders/',list_orders),
     path('create-orders/',create_orders),          
              
]