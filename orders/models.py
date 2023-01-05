from django.db import models

CHOICES = [
    ('cash','cash'),
    ('card','card'),  
]

class Orders(models.Model):
    client = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    creation_time = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(choices=CHOICES ,max_length=4)   
    
    def __str__(self):
        return self.client
    
    
    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'
class Category(models.Model):
    name = models.CharField(max_length= 60 ,unique=True )   