from django.shortcuts import render

# Create your views here.
def novedades(request):
    return render(request,'novedades/novedades.html')
