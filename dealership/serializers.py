from rest_framework import serializers
from .models import Car, CarImage


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ['id', 'image']


class SimpleCarSerializer(serializers.ModelSerializer):
    #TODO: images = serializers.StringRelatedField(many=True)
    images = CarImageSerializer(read_only=True,many=True)
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'mileage', 'price', 'year','images']



class CarSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(read_only=True,many=True)
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'mileage', 'price', 'year', 'power', 'fuel', 'price', 'description', 'date_added', 'images']
        



    # id = serializers.IntegerField()
    # make = serializers.CharField(max_length=100)
    # model = serializers.CharField(max_length=100)
    # mileage = serializers.IntegerField()
    # price = serializers.IntegerField()
