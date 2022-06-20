from django.db import models
from django.core.validators import MinValueValidator
import datetime

# Create your models here.
class CarModel(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    mileage = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1)])

    TRANSMISSION = (
                ('Ръчна','Ръчна'),
                ('Автоматична','Автоматична'),
                ('Полуавтоматична', 'Полуавтоматична')
    )

    CAR_TYPES = (
        ('Ван', 'Ван'),
        ('Джип', 'Джип'),
        ('Кабрио', 'Кабрио'),
        ('Комби', 'Комби'),
        ('Купе', 'Купе'),
        ('Миниван', 'Миниван'),
        ('Пикап', 'Пикап'),
        ('Седан', 'Седан'),
        ('Стреч лимузина', 'Стреч лимузина'),
        ('Хечбек', 'Хечбек'),
    )

    ENGINE_TYPES = (
        ('Бензинов', 'Бензинов'),
        ('Дизелов', 'Дизелов'),
        ('Електрически', 'Електрически'),
        ('Хибриден', 'Хибриден')
    )


    transmission = models.CharField(max_length=50, choices=TRANSMISSION)
    engine_type = models.CharField(max_length=50, choices=ENGINE_TYPES)
    type = models.CharField(max_length=50, choices=CAR_TYPES)
    YEAR_CHOICES = [(r,r) for r in range(1980, datetime.date.today().year+1)]
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    power = models.IntegerField(validators=[MinValueValidator(1)])
    fuel = models.FloatField(validators=[MinValueValidator(0)])
    price = models.IntegerField(validators=[MinValueValidator(1)])
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        abstract=True

    def __str__(self):
        return self.make



class Car(CarModel):
    date_added = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["-date_added"]

class CarImage(models.Model):
    Car = models.ForeignKey(
        Car, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(
        upload_to='dealership/images') # validators=[validate_file_size]

    # def __str__(self):
    #     return self.image.url


class CarEvaluation(CarModel):
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=12)
    date_submitted = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='dealership/images')

    class Meta:
        ordering = ["-date_submitted"]
