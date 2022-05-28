from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Car, CarEvaluation
from .serializers import CarSerializer, SimpleCarSerializer, CarEvaluationSerializer

# TODO: only show urls to each image when inspecting a car detail page, otherwise - only show the first image?

class CarList(generics.ListAPIView):
    queryset = Car.objects.prefetch_related('images').all()
    serializer_class = SimpleCarSerializer

# Fix this
class CarDetail(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarEvaluate(generics.CreateAPIView):
    serializer_class = CarEvaluationSerializer
    