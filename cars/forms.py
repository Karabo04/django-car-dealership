from django import forms
from django.forms import ModelForm
from .models import *

class SaleForm(ModelForm):
    class Meta:
        model= Sale
        fields = ['car', 'price', 'date_sold', 'sales_person', 'status']
        widgets = {
            'date_sold': forms.DateInput(attrs={'type': 'date'}),
        }