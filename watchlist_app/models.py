from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class streamPlatform(models.Model): #like prime video, netflix etc
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=100)
    url = models.URLField(max_length=150)

    def __str__(self):
        return self.name

class watchList(models.Model):
    title = models.CharField(max_length=30)
    storyLine = models.CharField(max_length=60)
    platform = models.ForeignKey(streamPlatform, on_delete=models.CASCADE, related_name='watchlist')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey(watchList, on_delete=models.CASCADE, related_name='reviews')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return str(self.rating) + ' | ' + self.watchlist.title #WE NEED TO CONVERT THIS INTO A STRING.