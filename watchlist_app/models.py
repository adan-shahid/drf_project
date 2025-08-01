from django.db import models

# Create your models here.
class watchList(models.Model):
    title = models.CharField(max_length=30)
    storyLine = models.CharField(max_length=60)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class streamPlatform(models.Model): #like prime video, netflix etc
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=100)
    url = models.URLField(max_length=150)

    def __str__(self):
        return self.name