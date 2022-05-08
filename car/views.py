from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer

# Create your views here.

@api_view()
def car_list(request):
    queryset = Car.objects.all()
    serializer = CarSerializer(queryset,many=True)
    return Response(serializer.data)

