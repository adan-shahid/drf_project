from django.contrib import admin
from .models import CustomUser
# Register your models here.
admin.site.site_header = 'My Project Administration'
admin.site.site_title = 'My Project Portal'
admin.site.index_title = 'Welcome to my project admin'

admin.site.register(CustomUser)