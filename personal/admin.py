from django.contrib import admin
from .models import *
# Register your models here.

class PersonalAdmin(admin.ModelAdmin):
    list_display = ['name', 'ap', 'am','area', 'estado']
    search_fields = ['name', 'ap', 'am', 'area']
    list_filter = ["area","estudio"]
    list_per_page = 5

admin.site.register(personal,PersonalAdmin)
admin.site.register(Area)
admin.site.register(Estudio)
