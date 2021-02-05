from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm # esto son los formularios que nos da django
from django.contrib.auth.models import User


class CustomUserForm(UserCreationForm):
    class Meta :
        model = User
        fields =['username', 'password1', 'password2']

class Category(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Category, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("detail", kwargs={
    #         'slug': self.slug
    #     })   

    def get_absolute_url(self):
        return reverse("detail")

class Post(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    obs = models.CharField(max_length=255)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='static',blank=True, default='proced.jpg')
    fecha = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("detail", kwargs={
            'slug': self.slug
        })
        
    def get_like_url(self):
        return reverse("like", kwargs={
            'slug': self.slug
        })
          
    @property
    def get_comentario_count(self):
        return self.comentario_set.all().count()
    @property
    def get_postview_count(self):
        return self.postview_set.all().count()
    @property
    def get_like_count(self):
        return self.like_set.all().count()


class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()

    def __str__(self):
        return self.user.username    

# numero de vistas del post
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
# cantidad de likes del post
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



