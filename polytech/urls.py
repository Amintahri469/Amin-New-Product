from django.urls import re_path as url
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('products.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)