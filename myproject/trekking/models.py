
from django.db import models

class User(models.Model):
    fam = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    otc = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

class Coordinates(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

class Level(models.Model):
    winter = models.CharField(max_length=10, blank=True)
    summer = models.CharField(max_length=10, blank=True)
    autumn = models.CharField(max_length=10, blank=True)
    spring = models.CharField(max_length=10, blank=True)

class Image(models.Model):
    data = models.TextField()
    title = models.CharField(max_length=100)

class Pass(models.Model):
    beauty_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    other_titles = models.CharField(max_length=100, blank=True)
    connect = models.TextField(blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.OneToOneField(Coordinates, on_delete=models.CASCADE)
    level = models.OneToOneField(Level, on_delete=models.CASCADE)
    images = models.ManyToManyField(Image)
