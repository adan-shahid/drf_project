from django.db import models
from django.conf import settings
# Create your models here.
class Company(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='companies')
    name = models.CharField(max_length=200)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        unique_together = ['user', 'name']

    def __str__(self):
        return self.name