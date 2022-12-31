#Import from the core django
from django import forms
from django.forms import ModelForm
#Import from local app/library
from django.contrib.auth.models import User


# class LoginForm(forms.ModelForm):
#       class Meta:
#         model= User
#         fields=  ['username' ,'password'  ]  

class RegistreationForm(ModelForm):
      class Meta:
        model= User
        fields=  ['id', 'username', 'email', 'password' ,'first_name','last_name' ] 
        # fields= '__all__'  
               # this function will be used for the server side validation
      def clean(self):
          # data from the form is fetched using super function
          super(RegistreationForm, self).clean()
          # extract the fields ield from the data

          username = self.cleaned_data['username']
          password = self.cleaned_data['password']
          print('test point')
      
          # return any errors if found.
          return self.cleaned_data  


