from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from .forms import Contact_Form
from django.http import HttpRequest

# Create your views here.

class Contact_Form_View(HttpRequest):

    def contact_form(request):
        contact = Contact_Form()
        return render(request, 'Contact/contact.html', {'form':contact})
    
    def check_form(request):
        contact = Contact_Form(request.POST)
        if contact.is_valid():
            contact.save()
            contact = Contact_Form()
        return render(request, 'Contact/contact.html', {'form':contact, 'check':'check'})