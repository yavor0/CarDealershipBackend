from django.contrib import admin
from django.utils.html import format_html
from . import models
# Register your models here.

# TODO: when deleting a car from admin the image (the file) associated with that car doesn't get deleted. Fix that

class CarImageInline(admin.TabularInline):
    model = models.CarImage
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail" />')
        return ''


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['make', 'model', 'transmission', 'year', 'power', 'fuel', 'price', 'date_added']
    list_editable = ['transmission', 'year', 'price']
    list_per_page = 20
    search_fields = ['make', 'model']
    list_filter = ['make']
    inlines = [CarImageInline]