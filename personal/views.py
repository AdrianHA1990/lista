from django.shortcuts import render
from .models import personal
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import PersonalForm

# Create your views here
class inicio(TemplateView):
    template_name = 'paginas_base/inicio.html'

class lista(ListView):
    template_name = 'paginas_base/listado.html'
    model = personal
    ordering = "id"
    queryset = personal.objects.all()
    context_object_name = "Personal"

class registro(CreateView):
    template_name = 'paginas_base/registro.html'
    model = personal
    form_class = PersonalForm

    def get_success_url(self, **kwargs):
        return reverse("personal_app:lista")

class editar(UpdateView):
    template_name = 'paginas_base/editar.html'
    model = personal
    form_class = PersonalForm
    pk_url_kwarg = "pk"

    def get_success_url(self, **kwargs):
        return reverse("personal_app:lista")

class eliminar(DeleteView):
    template_name = 'paginas_base/eliminar.html'
    model = personal
    pk_url_kwarg = "pk"

    def get_success_url(self, **kwargs):
        return reverse("personal_app:lista")



