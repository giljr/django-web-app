from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.CharField(max_length=100)
    genre = models.CharField(choices=Genre.choices, max_length=5)
    biography = models.CharField(max_length=1000)
    year_formed = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.BooleanField(default=True)
    official_homepage = models.URLField(null=True, blank=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.name}'


class Listing(models.Model):

    class Type(models.TextChoices):
        RECORDS = 'R'
        CLOTHING = 'C'
        POSTERS = 'P'
        MISC = 'M'

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    sold = models.BooleanField(default=False)
    year = models.IntegerField(
        null=True,
        validators=[MinValueValidator(1900),
                    MaxValueValidator(2021)])
    type = models.CharField(choices=Type.choices, max_length=5)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}'
