#Import from the core django
from django import forms
#Import from local app/library
from item.models import Product,Order,Customer

#Item
class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields= '__all__'

#Order
class OrderForm(forms.ModelForm):
      class Meta:
        model= Customer
        fields= '__all__'   

class StatusForm(forms.ModelForm):
      class Meta:
        model=Order
        fields=  ['order_status']       
        
          