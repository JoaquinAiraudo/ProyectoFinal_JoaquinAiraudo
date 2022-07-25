from django.shortcuts import render
from .models import Post
from django.views.generic.base import TemplateView

# Create your views here.

class Blog_view(TemplateView):
    tmpl = 'Blog/blog.html'

    def get(self, request, *arg, **kwargs):
        return render(request, self.tmpl, {'posts': Post.objects.all()})
