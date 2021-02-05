from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class Frecuentes(models.Model):
    titulo = models.CharField(max_length=150, unique=True)
    contenido = RichTextField()
    fecha = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Frecuentes, self).save(*args, **kwargs)        

    def get_absolute_url(self):
        return reverse("detail")