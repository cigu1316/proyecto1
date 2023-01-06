from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100,)
    price = models.FloatField()
    stock = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
       
    
class Category(models.Model):
    name = models.CharField(max_length= 60 ,unique=True )    