from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
admin.site.site_header = 'My Project Administration'
admin.site.site_title = 'My Project Portal'
admin.site.index_title = 'Welcome to my project admin'

admin.site.register(CustomUser)

class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'created_at']
    ordering = ['email']