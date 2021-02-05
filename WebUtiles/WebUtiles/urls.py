from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from apps.linksutiles import views
from apps.procedimientos.views import *
from django.contrib.auth import views as auth_views

handler404 = 'apps.procedimientos.views.view_404'

urlpatterns = [
    # path generales
    path('pruebapiloto/', admin.site.urls),
    # path('', views.index),
    path('procedimientos', procedimientos),

    # path web utiles    
    path('', views.AllWeb.as_view()),
    path('link_new/', views.AddWeb.as_view(), name='link_new'),
    path('<slug:slug>/delete_web', views.DeleteWeb.as_view(), name='delete_web'),
    path('<slug:slug>/up_web', views.UpdateWeb.as_view(), name='up_web'),

    # path procedimientos   
    path('create', PostCreateView.as_view(), name='create'),
    path('procedimientos/<slug>/delete', PostDeleteView.as_view(), name='delete'),
    path('procedimientos/<slug:slug>/update/', PostUpdateView.as_view(), name='update'),
    path('procedimientos/<slug:slug>',PostDetailView, name="detail"),
    path('like/<slug>', like, name="like"),

    # path categorias
    path('categorias', DetalleCategoria.as_view(), name='categorias'),
    path('categoria_nueva/', AddCategoryView.as_view(), name='categoria_nueva'),
    path('procedimientos/<slug:slug>/delete_categoria', DeleteCategoryView.as_view(), name='delete_categoria'),
    path('procedimientos/<slug:slug>/up_categoria', UpdateCategoryView.as_view(), name='up_categoria'),
    
    # path usuario
    path('accounts/', include('django.contrib.auth.urls' )), 
    path('registrar/', registro_usuario, name='registro_usuario'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('', include('apps.pregfrecuentes.urls')),
    path('', include('apps.novedades.urls')),

    # path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
    #  name='password_reset_done'),

    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    #  name='password_reset_complete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)


