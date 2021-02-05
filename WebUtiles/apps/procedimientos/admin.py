from django.contrib import admin

# Register your models here.
from .models import Post, Comentario, PostView, Like,Category

admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(PostView)
admin.site.register(Like)
admin.site.register(Category)
