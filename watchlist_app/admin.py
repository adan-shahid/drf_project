from django.contrib import admin
from .models import watchList, streamPlatform, Review

# Register your models here.
admin.site.register(watchList)
admin.site.register(streamPlatform)
admin.site.register(Review)
