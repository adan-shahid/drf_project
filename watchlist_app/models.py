from django.db import models

# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name