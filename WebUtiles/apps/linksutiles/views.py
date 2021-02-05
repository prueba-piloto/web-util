from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import Template, Context
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,View
from django.db.models import Q,Count

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


#links:
class AllWeb(ListView):
    model = WebUtil
    template_name = 'index.html'
    fields = '__all__'
    
    def get_queryset(self,*args,**kwargs):
        webs = WebUtil.objects.all().order_by('-update')
        queryset = self.request.GET.get("buscar")
        #filtra lo que yo escribo en el buscador
        if queryset:
            webs = WebUtil.objects.filter(
                Q(nombre__icontains = queryset) |
                Q(obs__icontains = queryset)
            ).distinct()
        context = {
            'web':webs
        }
        return webs

# class DetailWeb(DetailView):
#     model = WebUtil
#     template_name = 'weblinks/detail_WebUtil.html'

class AddWeb(CreateView):
    model = WebUtil
    template_name = 'weblinks/add_WebUtil.html'
    success_url = "/"
    fields = '__all__'

class UpdateWeb(UpdateView):
    model = WebUtil
    template_name = 'weblinks/up_WebUtil.html'
    success_url = "/"
    fields = '__all__'

class DeleteWeb(DeleteView):
    model = WebUtil
    template_name = 'weblinks/delete_WebUtil.html'
    success_url = '/'