from django.db import models
from django.urls import reverse

# Create your models here.
class Lego(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    pieces = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('lego-detail', kwargs={'lego': self.id})
    
class Wishlist(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('wishlist-detail', kwargs={'pk': self.id})
