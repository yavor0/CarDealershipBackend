from rest_framework import serializers
from .models import Car, CarImage, CarEvaluation


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
        fields = ['id', 'make', 'model', 'mileage', 'price', 'year', 'power', 'fuel', 'description', 'date_added', 'images']
        
class CarEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarEvaluation
        fields = ['id', 'email', 'phone', 'make', 'model', 'mileage', 'price', 'year', 'power', 'fuel', 'description']
        


    # id = serializers.IntegerField()
    # make = serializers.CharField(max_length=100)
    # model = serializers.CharField(max_length=100)
    # mileage = serializers.IntegerField()
    # price = serializers.IntegerField()
