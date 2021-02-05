from django.urls import path
from . import views

urlpatterns = [
    path('novedades', views.novedades),
]
