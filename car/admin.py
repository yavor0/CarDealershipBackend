from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['make', 'model', 'transmission', 'year', 'power', 'fuel', 'price', 'date_added']
    list_editable = ['transmission', 'year', 'price']
    list_per_page = 20
    search_fields = ['make', 'model']
    list_filter = ['make']

