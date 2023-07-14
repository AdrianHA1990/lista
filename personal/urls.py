from django.urls import path
from django.contrib.staticfiles.urls import static
from . import views
from django.conf import settings

app_name = "personal_app"

urlpatterns = [
    path('', views.inicio.as_view(), name='inicio'),
    path('lista', views.lista.as_view(), name='lista'),
    path('registro', views.registro.as_view(), name='registro'),
    path('editar/<pk>', views.editar.as_view(), name='editar'),
    path('eliminar/<pk>', views.eliminar.as_view(), name='eliminar'),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)