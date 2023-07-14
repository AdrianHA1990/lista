from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.auth import views as auth_view

app_name = "clientes_app"

urlpatterns = [
    path('', views.home.as_view(), name="home"),
    path('login/', auth_view.LoginView.as_view(template_name="crud/login.html"), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name="crud/login.html"), name="logout"),
    path('compras/', views.compras.as_view(), name="compras"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)