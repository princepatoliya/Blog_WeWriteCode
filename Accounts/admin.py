from django.contrib import admin

from .models import(
    Profile,
)
# Register your models here.

class AdminProfile(admin.ModelAdmin):
    list_display=('id', 'user', 'is_verified')
    


admin.site.register(Profile, AdminProfile)