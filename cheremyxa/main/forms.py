from django import forms
from .models import *


class ProductKForm(forms.ModelForm):
    class Meta:
        model = Product_K
        fields = ['name', 'weight', 'price', 'composition', 'image']

class ProductBForm(forms.ModelForm):
    class Meta:
        model = Product_B
        fields = ['name', 'weight', 'price', 'composition', 'image']

class ProductCForm(forms.ModelForm):
    class Meta:
        model = Product_C
        fields = ['name', 'weight', 'price', 'composition', 'image']