from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Items(models.Model):
    content = models.CharField(max_length=200)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.content
    
    class Meta:
        ordering=["-created_at"]



class Pricing(models.Model):
    title = models.CharField(max_length=100)
    amount = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=False)
    items = models.ManyToManyField(Items, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering=["created_at"]


class FrequnlyQuestion(models.Model):
    question = models.TextField()
    answerr = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
    
    class Meta:
        ordering=["created_at"]

class Skills(models.Model):
    title = models.CharField(max_length=100, default="skl")
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering=["created_at"]

class Star(models.Model):
    count = models.PositiveIntegerField(default=3)

    def __str__(self):
        return str(self.count)
    
    def count_object(self):
        return range(self.count)

class Team(models.Model):
    image = models.ImageField(upload_to="profile", default="default.jpg")
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(default="test description")
    status = models.BooleanField(default=True)
    skills = models.ManyToManyField(Skills)
    stars = models.ForeignKey(Star, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.username
    
    class Meta:
        ordering=["created_at"]


class Leader(models.Model):
    image = models.ImageField(upload_to="profile", default="default.jpg")
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(default="test description")
    status = models.BooleanField(default=True)
    skills = models.ManyToManyField(Skills)
    twitter = models.CharField(max_length=255, default="#")
    facebook = models.CharField(max_length=255, default="#")
    instagram = models.CharField(max_length=255, default="#")
    linkedin  = models.CharField(max_length=255, default="#")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.username
    
    class Meta:
        ordering=["created_at"]







