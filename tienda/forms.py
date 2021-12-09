from django.forms import ModelForm, fields, DateInput
from tienda.models import TarjetaRegalo, User
from django import forms


class UserForm(ModelForm):
    
    class Meta:
        model = User
        fields = ['username','email' ,'password' , 'first_name', 'last_name','imagen']

class CrearTarjetaForm(ModelForm):
    
    class Meta:
        model = TarjetaRegalo
        fields =['saldo','codigo']



class AñadirSaldoForm(forms.Form):
    codigo = forms.CharField(initial="ponga su codigo")



class ContactForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea())
    sender = forms.EmailField(required=True)