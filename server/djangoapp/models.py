"""Database models for the djangoapp application."""

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class CarMake(models.Model):
    """Represent a car manufacturer."""

    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        """Return the car make name."""
        return self.name


class CarModel(models.Model):
    """Represent a car model."""

    car_make = models.ForeignKey(
        CarMake,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("WAGON", "Wagon"),
    ]

    type = models.CharField(
        max_length=10,
        choices=CAR_TYPES,
        default="SUV",
    )

    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015),
        ],
    )

    def __str__(self):
        """Return the car model name."""
        return self.name
