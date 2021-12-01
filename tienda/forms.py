from django.forms import ModelForm, fields, DateInput
from tienda.models import User


class UserForm(ModelForm):
    
    class Meta:
        model = User
        fields = ['username','email' ,'password' , 'first_name', 'last_name',]
