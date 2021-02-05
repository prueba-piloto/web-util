from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,View
from django.db.models import Q,Count
from .forms import *
from django.contrib import messages

# Create your views here.
class AllFrecuentes(ListView):
    model = Frecuentes
    template_name = 'frecuentes/frecuentes.html'
    fields = '__all__'

    def get_queryset(self,*args,**kwargs):
        frecuentes = Frecuentes.objects.all().order_by('-update')
        queryset = self.request.GET.get("buscar")
        #filtra lo que yo escribo en el buscador
        if queryset:
            frecuentes = Frecuentes.objects.filter(
                Q(titulo__icontains = queryset) |
                Q(contenido__icontains = queryset)
            ).distinct()
        context = {
            'frecuentes':frecuentes
        }
        return frecuentes

class AddFrecuentes(CreateView):
    form_class = PregForm
    model = Frecuentes
    template_name = 'frecuentes/add_frecuentes.html'
    success_url = "/frecuentes"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'Crear'
        })
        return context

class UpdateFrecuentes(UpdateView):
    model = Frecuentes
    template_name = 'frecuentes/up_frecuentes.html'
    success_url = "/frecuentes"
    fields = '__all__'

class DeleteFrecuentes(DeleteView):
    model = Frecuentes
    template_name = 'frecuentes/delete_frecuentes.html'
    success_url = '/frecuentes'