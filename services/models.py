from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Specials(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField(default="test")
    status = models.BooleanField(default=True)
    #icon = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Services(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="service", default="services.png")
    stitle = models.CharField(max_length=200)
    content = models.TextField()
    ltitle = models.CharField(max_length=255)
    desc1 = models.TextField()
    desc2 = models.TextField()
    counted_view = models.PositiveIntegerField(default=0)
    total_like = models.PositiveIntegerField(default=0)
    category = models.ManyToManyField(Category)
    specials = models.ManyToManyField(Specials)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.stitle
