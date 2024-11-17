from django.db import models
import datetime

class Person(models.Model):
    """Represents any person."""
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=datetime.date(2000, 1, 1))
    motorbikes = models.ManyToManyField('Motorbike', through='Ride')

    def __str__(self):
        return self.name


class Motorbike(models.Model):
    """Represents a motorbike with details about it."""
    name = models.CharField(max_length=100)
    engine_capacity = models.IntegerField()  # in cc's
    description = models.TextField()
    is_automatic = models.BooleanField(default=False) #True is automatic, False if manual

    def __str__(self):
        return f"{self.name} ({self.engine_capacity}cc, {'Automatic' if self.is_automatic else 'Manual'})"


class Ride(models.Model):
    """Through class that represents which people ride which bikes"""
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    motorbike = models.ForeignKey(Motorbike, on_delete=models.CASCADE)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        favourite_status = 'is' if self.is_favourite else 'is not'
        return f"{self.person.name} rides {self.motorbike.name} and it {favourite_status} their favourite bike."