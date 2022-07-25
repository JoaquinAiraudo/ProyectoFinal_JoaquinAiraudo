from django.contrib import admin
from .models import Presidente, Ministro, Partido

# Register your models here.

class Presidente_admin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'partido', 'asume_cargo')
    search_fields = ('nombre', 'apellido', 'partido', 'asume_cargo')
    list_filter = ('partido',)
    date_hierarchy = 'asume_cargo'

admin.site.register(Presidente, Presidente_admin)

class Ministro_admin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cartera', 'asume_cargo')
    search_fields = ('nombre', 'apellido', 'cartera', 'asume_cargo')
    list_filter = ('cartera',)
    date_hierarchy = 'asume_cargo'

admin.site.register(Ministro, Ministro_admin)

class Partido_admin(admin.ModelAdmin):
    list_display = ('nombre', 'fundacion')
    search_fields = ('nombre', 'fundacion')
    date_hierarchy = 'fundacion'

admin.site.register(Partido, Partido_admin)