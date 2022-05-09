from django.db import models
from django.core.validators import MinValueValidator
import datetime

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    # CATEGORY = (
    #         ('New','New'),
    #         ('Used','Used')
    #     )
    # category = models.CharField(max_length=50, choices=CATEGORY)
    # image_main = models.ImageField(upload_to='images')
    # image1 = models.ImageField(upload_to='images', blank=True)
    # image2 = models.ImageField(upload_to='images', blank=True)
    # image3 = models.ImageField(upload_to='images', blank=True)
    # image4 = models.ImageField(upload_to='images', blank=True)
    # image5 = models.ImageField(upload_to='images', blank=True)

    mileage = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1)])

    TRANSMISSION = (
                ('Manual','Manual'),
                ('Automatic','Automatic')
    )

    transmission = models.CharField(max_length=50, choices=TRANSMISSION)
    type = models.CharField(max_length=50, null=True)
    YEAR_CHOICES = [(r,r) for r in range(1980, datetime.date.today().year+1)]
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    power = models.IntegerField(validators=[MinValueValidator(1)])
    fuel = models.FloatField(validators=[MinValueValidator(0)])
    price = models.IntegerField(validators=[MinValueValidator(1)])
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return self.make


class CarImage(models.Model):
    Car = models.ForeignKey(
        Car, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(
        upload_to='dealership/images') # validators=[validate_file_size]

    # def __str__(self):
    #     return self.image.__str__()
