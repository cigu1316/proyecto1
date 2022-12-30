from django.contrib import admin
from django.urls import path , include

from products.views import create_product,list_products,list_categories,create_category
                            
urlpatterns = [
      
    path('create-product/',create_product),
    path('list-products/',list_products),
    
    path('list-categories/',list_categories),
    path('create-category/<str:name>/',create_category),        
              
]

