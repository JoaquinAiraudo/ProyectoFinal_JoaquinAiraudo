from django.shortcuts import render
from .models import Services
from django.views.generic.base import TemplateView

# Create your views here.

class Services_view(TemplateView):
    tmpl = 'Services/services.html'

    def get(self, request, *arg, **kwargs):
        return render(request, self.tmpl, {'servicios': Services.objects.all()})

