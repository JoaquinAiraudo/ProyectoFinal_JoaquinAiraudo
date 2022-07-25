from django.urls import path
from .views import log_in, Register_view, log_out

urlpatterns = [
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('register/', Register_view.as_view(), name='register'),
]