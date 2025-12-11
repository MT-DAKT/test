from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=50)

class Groupe(models.Model):
    title = models.CharField(max_length=100)
