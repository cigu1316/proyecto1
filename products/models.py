from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100,verbose_name= 'nombre')
    price = models.FloatField (verbose_name= 'precio')
    stock = models.BooleanField(verbose_name= 'stock')
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
       
    
class Category(models.Model):
    name = models.CharField(max_length= 60 ,unique=True )    