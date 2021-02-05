from django import forms
from .models import Post, Category
import datetime
# from django.contrib.auth.forms import UserCreationForm # esto son los formularios que nos da django
# from django.contrib.auth.models import User
# class CustomUserForm(UserCreationForm):
#      class Meta :
#           model = User
#           fields =['username', 'password1', 'password2']


choices = Category.objects.all().values_list('nombre', 'nombre')
choice_list = []

for item in choices:
     choice_list.append(item)


class PostForm(forms.ModelForm):
     class Meta:
          model = Post
          fields = ['titulo','autor','imagen','contenido','obs', 'category']

          widgets = {
               'titulo':forms.TextInput(attrs={'class':'form-control'}),
               'autor':forms.TextInput(attrs={'class':'form-control', 'value':'','id':'identificador','type':'hidden'}),
               'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
               'imagen':forms.FileInput(attrs={'class':'form-control-file'}),
               'contenido':forms.Textarea(attrs={'class':'form-control'}),             
               'obs':forms.TextInput(attrs={'class':'form-control'}),             
          }