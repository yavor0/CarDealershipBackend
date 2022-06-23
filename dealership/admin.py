from django.contrib import admin
from django.utils.html import format_html
from django_object_actions import DjangoObjectActions
from . import models
from .mobile_upload.upload import MobileUploader
from pathlib import Path
import os
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
class CarAdmin(DjangoObjectActions, admin.ModelAdmin):
    def publish_this(self, request, obj):
        images = [os.path.join(Path(os.getcwd()).parent, "CarDealershipBackend", "media", Path(str(image.image))) for image in models.CarImage.objects.select_related().filter(Car=obj)]
        # print(images)
        uploader = MobileUploader()
        uploader.run(obj, images)

    publish_this.label = "Publish to mobile"  # optional
    publish_this.short_description = "Submit this car to mobile"  # optional

    change_actions = ('publish_this', )


    list_display = ['make', 'model', 'transmission', 'year', 'power', 'fuel', 'price', 'date_added']
    list_editable = ['transmission', 'year', 'price']
    list_per_page = 20
    search_fields = ['make', 'model']
    list_filter = ['make']
    inlines = [CarImageInline]
