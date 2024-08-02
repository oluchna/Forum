from django.contrib import admin
from .models import Post, Tag
from django.core.exceptions import ValidationError
# Register your models here.



admin.site.register(Post)

# admin.site.register(Post)
admin.site.register(Tag)