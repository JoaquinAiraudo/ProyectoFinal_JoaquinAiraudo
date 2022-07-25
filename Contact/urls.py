from django.urls import path
from .views import Contact_Form_View

urlpatterns = [
    path('', Contact_Form_View.contact_form, name='contact'),
    path('sav_cont/', Contact_Form_View.check_form, name='savecontact'),
]