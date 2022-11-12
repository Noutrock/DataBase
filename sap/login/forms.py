from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput
from django import forms

from login.models import ModelLogin


class formRegister(UserCreationForm):
   password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
   password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

   class Meta :
       model = User
       fields = ['username','password1','password2']
       help_texts = {k:"" for k in fields }
