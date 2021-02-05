from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from django.utils import timezone

# Create your models here.
class WebUtil(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    link = models.CharField(max_length=300)
    obs = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(WebUtil, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("detail")