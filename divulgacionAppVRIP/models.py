from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField('Nombre de Categoría', max_length=100, null=False, blank=False)
    estado = models.BooleanField('Activada/No Activada', default=True)
    fechaCreacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        db_table = 'categoria'
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    nombres = models.CharField('Nombre de Autor', max_length=255, null=False, blank=False)
    apellidos = models.CharField('Apellidos de Autor', max_length=255, null=False, blank=False)
    facebook = models.URLField('Facebook', null=True, blank=True)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    web = models.URLField('Web', null=True, blank=True)
    correo = models.EmailField('Correo Electrónico', null=False, blank=False)
    estado = models.BooleanField('Activo/No Activo', default=True)
    fechaCreacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        db_table = 'autor'
        managed = True
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "{0}, {1}".format(self.apellidos, self.nombres)


class Post(models.Model):
    titulo = models.CharField('Titulo', max_length=90, null=False, blank=False)
    slug = models.CharField('Slug', max_length=100, null=False, blank=False)
    descripcion = models.CharField('Descripción', max_length=100, null=False, blank=False)
    contenido = RichTextField()
    imagen = models.ImageField('Imagen del Tema',null=False, blank=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default=True)
    fechaCreacion = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        db_table = 'post'
        managed = True
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'
        ordering = ('-fechaCreacion', '-id')

    def __str__(self):
        return self.titulo

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    nombre = models.CharField('Nombre de Autor', max_length=255, null=False, blank=False)
    correo = models.EmailField('Correo Electrónico', null=False, blank=False)
    comentario = models.TextField('Comentario')
    fechaCreacion = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True) 
    estado = models.BooleanField('Publicado/No Publicado', default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        db_table = 'comment'
        managed = True
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ('-fechaCreacion', '-id')

    def __str__(self):
        return 'Comentado {} por {}'.format(self.comentario, self.nombre)

    def __unicode__(self):
        return 


