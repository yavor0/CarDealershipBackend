from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'mileage', 'price']
    # id = serializers.IntegerField()
    # make = serializers.CharField(max_length=100)
    # model = serializers.CharField(max_length=100)
    # mileage = serializers.IntegerField()
    # price = serializers.IntegerField()
