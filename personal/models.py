from django.db import models
from contextlib import nullcontext
from django.utils import timezone
from django.contrib.auth.models import User
# from crud_4.curso4.models import DatosBase


#Create your models here.

class DatosBase(models.Model):
    estado = models.BooleanField(default=True)
    fecha_reg = models.DateTimeField(auto_now_add=True)
    fecha_act = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)

    #no se toma en cuenta
    class Meta:
        abstract = True


class Area(DatosBase):
    nom_area = models.CharField(max_length=150, verbose_name="Area", null=False)

    def __str__(self):
            fila=self.nom_area
            return fila

class Estudio(DatosBase):
    nom_est = models.CharField(max_length=150, verbose_name="Area", null=False, blank=False)

    def __str__(self):
        fila=self.nom_est
        return fila

carrera=(
    ('Sistemas', 'Sistemas'),
    ('Contabilidad', 'Contabilidad'),
    ('Derecho', 'Derecho'),
    ('Adminsitracion', 'Administracion'),

)

class personal(DatosBase):
    name = models.CharField(max_length=100, verbose_name="Nombre", null=False, blank=False)
    ap = models.CharField(max_length=100, verbose_name="Apellido Paterno", null=False, blank=False)
    am = models.CharField(max_length=100, verbose_name="Apellido Materno", null=False, blank=False)
    foto = models.ImageField(upload_to='imagenes/', verbose_name="Foto", null=True, blank=True)
    area = models.ForeignKey(Area,verbose_name="Area",on_delete=models.CASCADE)
    estudio = models.ForeignKey(Estudio, verbose_name="Estudio", on_delete=models.CASCADE)
    Carrera = models.CharField(max_length=100, verbose_name="Carrera", choices=carrera)

    def __str__(self):
        fila=str(self.id) + "_" + self.name + "_" + self.ap + "_" + self.am
        return fila
    def delete(self, using=None, Keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()