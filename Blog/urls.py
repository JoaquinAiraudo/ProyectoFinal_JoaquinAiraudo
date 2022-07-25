from django.urls import path
from .views import Blog_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Blog_view.as_view() , name='blog'),
]

urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)