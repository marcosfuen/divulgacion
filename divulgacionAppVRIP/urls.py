from django.urls import path
from .views import index, generales, detallesPost
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('generales/', generales, name='generales'),
    path('<slug:slug>', detallesPost, name='detallesPost'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)