from django.shortcuts import render, redirect
from divulgacionAppVRIP.models import Post, Categoria, Comment
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .form import CommentForm
from django.db.models.aggregates import Count
from django.db.models import Q
from django.contrib import messages


# Create your views here.
def index(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado=True)
    if queryset:
        posts = Post.objects.filter(Q(titulo__icontains=queryset) | Q(descripcion__icontains=queryset) | Q(contenido__icontains=queryset)).distinct()

    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    comentariosPorTemas = Comment.objects.values_list('post__titulo', 'post__slug', 'post__descripcion', 'post__autor__nombres').annotate(dcount=Count('post__titulo')).order_by('post__titulo')
    return render(request, 'index.html', {'posts':posts, 'comentariosPorTemas':comentariosPorTemas})


def detallesPost(request, slug):
    # post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post, slug=slug)
    comment = post.comments.filter(estado=True, parent__isnull=True)
    if request.method == 'POST':
        commentForm = CommentForm(data=request.POST)
        if commentForm.is_valid():
            parent_obj = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                if parent_obj:
                    reply_comment = commentForm.save(commit=False)
                    reply_comment.parent = parent_obj
            new_comment = commentForm.save(commit=False)
            new_comment.post = post
            new_comment.save()
            messages.add_message(request,  messages.INFO, 'se adiciono el comentarios')
            return redirect('appVrip:detallesPost' , slug)
    else:
        commentForm = CommentForm()   
        storage = messages.get_messages(request)
        storage.used = False     
       
    return render(request, 'post.html', {'detallePost':post, 'comment': comment, 'commentForm':commentForm})


def generales(request):
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre__iexact='General'))
    comentariosPorTemas = Comment.objects.values_list('post__titulo', 'post__slug', 'post__descripcion', 'post__autor__nombres').annotate(dcount=Count('post__titulo')).order_by('post__titulo')
    return render(request, 'generales.html', {'posts':posts, 'comentariosPorTemas':comentariosPorTemas})