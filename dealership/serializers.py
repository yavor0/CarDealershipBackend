from rest_framework import serializers
from .models import Car, CarImage


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ['id', 'image']


class CarSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(many=True)
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'mileage', 'price', 'images']


    # id = serializers.IntegerField()
    # make = serializers.CharField(max_length=100)
    # model = serializers.CharField(max_length=100)
    # mileage = serializers.IntegerField()
    # price = serializers.IntegerField()
