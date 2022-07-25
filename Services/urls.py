from django.urls import path
from .views import Services_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Services_view.as_view() , name='services'),
]

urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)