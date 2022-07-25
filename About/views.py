from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class About_view(TemplateView):
    tmpl = 'About/about.html'

    def get(self, request, *arg, **kwargs):
        return render(request, self.tmpl, {'nombre': 'Joaquín Airaudo', 
        'vive': 'Montevideo - Uruguay',
        'profesion': 'Licenciado en Ciencia Política - UdelaR',
        'actualmente': 'Estudiante de Ciencias Económicas - UdelaR',
        'actualmente2': 'Estudiante de Programación en Python - Coderhouse',
        })