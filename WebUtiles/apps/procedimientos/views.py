from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,View
from .models import *
from django.db.models import Q,Count
from .forms import PostForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator #para la paginacion


# Create your views here.
def procedimientos(request):    
    queryset = request.GET.get("buscar")
    posts = Post.objects.all().order_by('-update')
    cantidad = Post.objects.count()
    order_by = request.GET.get('order_by_asc')
    order_by_d = request.GET.get('order_by_desc')

    order_by_ac = request.GET.get('order_by_ac')
    order_by_ac2 = request.GET.get('order_by_ac2')

   
    #filtra lo que yo escribo en el buscador
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(obs__icontains = queryset)
        ).distinct()
        cantidad = len(posts)
    
    paginator = Paginator(posts,10) #numero de paginas a mostrar
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    if order_by:
        posts = Post.objects.filter().order_by('category')       
    if order_by_d:
        posts = Post.objects.filter().order_by('-category')

    if order_by_ac:
        posts = Post.objects.filter().order_by('update')
    if order_by_ac2:
        posts = Post.objects.filter().order_by('-update')    

    
        
    context = {
        'post':posts,'cantidad':cantidad,'order_by':order_by,'order_by_ac':order_by_ac
    }
    return render(request, 'procedimientos.html', context)


def PostDetailView(request, slug):
    # post = Post.objects.get(
    #     slug = slug
    # )
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'procedimientos/post_detail.html',{'detail':post})


class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'Crear'
        })
        return context

class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'Actualizar'
        })
        return context

class PostDeleteView(DeleteView):
    model = Post
    success_url = "/procedimientos"

def view_404(request,exception):
    return render(request, '404.html')

def registro_usuario(request):
    data= {
        'form': CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid(): # con esto pregunto si el formulario es valido
            formulario.save()
            # Ahora lo que hago es si es correcto lo redirijo voy a importar arriba login ,authenticate
            username = formulario.cleaned_data['username'] # con .cleaned_data lo que hago es obtener los valores
            password= formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password) # con esto se autenfica ahora se hace el login
            login(request,user)
            return render(request, "index.html")       
        else:
            messages.warning(request,"Ha introducido mal los valores")
    return render(request, 'registration/registrar.html', data)


def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_qs = Like.objects.filter(user=request.user, post=post)
    if like_qs.exists():
        like_qs[0].delete()
        return redirect('detail',slug=slug)
    Like.objects.create(user=request.user, post=post)
    return redirect('detail',slug=slug)

#categoria:
class DetalleCategoria(ListView):
    model = Category
    template_name = 'procedimientos/list_category.html'
    fields = '__all__'

class AddCategoryView(CreateView):
    model = Category
    template_name = 'procedimientos/add_category.html'
    success_url = "/categorias"
    fields = '__all__'

class UpdateCategoryView(UpdateView):
    model = Category
    template_name = 'procedimientos/up_category.html'
    success_url = "/categorias"
    fields = '__all__'

class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'procedimientos/delete_category.html'
    success_url = '/categorias'