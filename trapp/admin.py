from django.contrib import admin

# Register your models here.
from .models import place,news

admin.site.register(place)
admin.site.register(news)