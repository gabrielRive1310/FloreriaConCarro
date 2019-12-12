from django.contrib import admin
from .models import Flor, Estado

# Register your models here.

class FlorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'valor', 'descripcion', 'estado', 'stock']
    search_fields = ['nombre']
    list_filter = ['estado']
    list_per_page = 20

admin.site.register(Estado)
admin.site.register(Flor, FlorAdmin)