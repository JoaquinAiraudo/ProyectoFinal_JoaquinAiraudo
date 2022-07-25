from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class Home_view(TemplateView):
    tmpl = 'Home/home.html'

    def get(self, request, *arg, **kwargs):
        return render(request, self.tmpl, {
                                            'title1':'POLITICAL SCIENCE',
                                            'content1':'Tu espacio de consulta',
                                            'title2':'Una web entre todos y para todos',
                                            'content2':'PS/Blog, un espacio que construimos entre todos gracias a nuestros aportes',})