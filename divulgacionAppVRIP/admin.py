from django.contrib import admin
from .models import Categoria, Autor, Post, Comment
from django.contrib.admin.templatetags.admin_modify import prepopulated_fields_js
# from simple_log.conf import settings
# from simple_log.models import SimpleLog

# from import_export import resources
# from import_export.admin import ImportExportModelAdmin


# Register your models here.
# class CategoriaResources(resources.ModelResource):
#     class Meta:
#         model = Categoria
       
# class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     search_file = ['nombre']
#     list_display = ('nombre', 'estado', 'fechaCreacion',)
#     resources_class = CategoriaResources

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'estado', 'fechaCreacion',)
    

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos', 'correo']
    list_display = ('nombres', 'apellidos', 'correo', 'estado', 'fechaCreacion',)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('titulo',)}
    search_fields = ['titulo', 'slug', ]
    list_display = ('titulo', 'estado', 'fechaCreacion',)

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'correo', 'comentario', 'fechaCreacion', 'estado']
    list_display = ('estado', 'nombre', 'correo', 'comentario', 'fechaCreacion')

# class SimpleLogAdmin(admin.ModelAdmin):
#     search_fields = ['action_time', 'content_type', 'user', 'user_repr', 'user_ip', 'object_id', 'object_repr', 'old', 'new', 'change_message']
#     list_display = ('action_time', 'user_repr', 'user_ip', 'object_repr', 'action_flag', 'old', 'new', 'change_message')



admin.site.register(Autor, AutorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
# admin.site.register(SimpleLog, SimpleLogAdmin)

admin.site.site_header = 'Analizando - Administración'
admin.site.site_title = 'Sistema de Analizando - Administración'
