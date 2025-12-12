from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=5, choices=Genre.choices)
    biography = models.CharField(max_length=1000)
    year_formed = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2025)])
    active = models.BooleanField(default=True)
    officiel_homepage = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Groupe(models.Model):
    class ListingType(models.TextChoices):
        RECORDS = 'R'
        CLOTHING = 'C'
        POSTERS = 'P'
        MISC = 'M'

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    sold = models.BooleanField(default=False)
    year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2025)])
    type = models.CharField(choices=ListingType.choices, max_length=5)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
