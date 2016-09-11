"""
Register the models here.
"""

from django.contrib import admin
from .models import Photo

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 3


admin.site.register(Photo)
