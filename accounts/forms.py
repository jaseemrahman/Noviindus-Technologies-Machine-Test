#Import from the core django
from django.forms import ModelForm
#Import from local app/library
from django.contrib.auth.models import User


class RegistreationForm(ModelForm):
      class Meta:
        model= User
        fields=  ['id', 'username', 'email', 'password' ,'first_name','last_name' ] 
      # def clean(self):
      #     super(RegistreationForm, self).clean()
      #     return self.cleaned_data  


