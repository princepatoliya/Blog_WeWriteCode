from django.contrib import admin
from .models import (
    BlogModel,
)
# Register your models here.

class AdminBlogModel(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'update_at',)

admin.site.register(BlogModel, AdminBlogModel)