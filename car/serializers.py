from rest_framework import serializers

class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    make = serializers.CharField(max_length=100)
    model = serializers.CharField(max_length=100)
    mileage = serializers.IntegerField()
    price = serializers.IntegerField()
