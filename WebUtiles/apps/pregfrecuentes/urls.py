from django.urls import path
from . import views

urlpatterns = [
    path('frecuentes', views.AllFrecuentes.as_view(), name="frecuentes"),
    path('create_frecuentes/', views.AddFrecuentes.as_view(), name='create_frecuentes'),
    path('frecuentes/<slug:slug>/delete_frecuentes', views.DeleteFrecuentes.as_view(), name='delete_frecuentes'),
    path('frecuentes/<slug:slug>/up_frecuentes', views.UpdateFrecuentes.as_view(), name='up_frecuentes'),
]
