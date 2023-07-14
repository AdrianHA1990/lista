from django.shortcuts import render
from .models import *
from django.http import HttpResponse
#from .forms  import ClientesForm
from django.views.generic import TemplateView
from django.views.generic import *
# from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class home(LoginRequiredMixin, TemplateView):
    template_name = 'crud/home.html'
    login_url = 'clientes_app:login'


class compras(TemplateView):
    template_name = 'crud/compras.html'

