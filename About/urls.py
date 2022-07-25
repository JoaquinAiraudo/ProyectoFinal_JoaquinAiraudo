from django.urls import path
from .views import About_view

urlpatterns = [
    path('', About_view.as_view(), name='aboutme'),
]