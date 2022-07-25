from django.urls import path
from .views import Legal_view, Privacity_view

urlpatterns = [
    path('legal', Legal_view.as_view(), name='legal'),
    path('privacity', Privacity_view.as_view(), name='privacity'),
]