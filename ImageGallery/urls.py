"""ImageGallery URL Configuration
The `urlpatterns` list routes URLs to views.
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
                  url(r'^imagegallery/', include('image_gallery.urls')),  # this line added
                  url(r'^admin/', admin.site.urls),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
