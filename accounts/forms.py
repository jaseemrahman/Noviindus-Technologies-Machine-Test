#Import from the core django
from django import forms
#Import from local app/library
from django.contrib.auth.models import User


# class LoginForm(forms.ModelForm):
#       class Meta:
#         model= User
#         fields=  ['username' ,'password'  ]  

class RegistreationForm(forms.ModelForm):
      class Meta:
        model= User
        fields=  ['id', 'username', 'email', 'password' ,'first_name','last_name' ] 
        # fields= '__all__'  
