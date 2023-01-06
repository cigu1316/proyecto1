from django import forms

class ProductsForm(forms.Form):
    name = forms.CharField(max_length=100)
    price =forms.FloatField()
    stock = forms.BooleanField(required=False)
    