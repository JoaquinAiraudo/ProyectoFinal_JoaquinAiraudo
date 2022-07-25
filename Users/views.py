from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

def log_in(request):     
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user_username = form.cleaned_data.get('username')
            user_password = form.cleaned_data.get('password')
            user = authenticate(username=user_username, password=user_password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Usuario no encontrado')
        else:
            messages.error(request, 'Información incorrecta')    

    form = AuthenticationForm()
    return render(request, 'Users/login.html', {'form' : form})



class Register_view(View):
    tmpl = 'Users/register.html'

    def get(self, request, *arg, **kwargs):
        form = UserCreationForm()
        return render(request, self.tmpl, {'form' : form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form = UserCreationForm(request.POST)
            user = form.save()
            login(request, user)
            return redirect ('home')
        else:
            for m in form.error_messages:
                messages.error(request, form.error_messages[m])
            
            return render(request, self.tmpl, {'form' : form})


def log_out(request):
    logout(request)
    return redirect('home')