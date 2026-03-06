from django.contrib import admin
from .models import Tag
from .models import Recipe

# Register your models here.
admin.site.register(Tag)
admin.site.register(Recipe)