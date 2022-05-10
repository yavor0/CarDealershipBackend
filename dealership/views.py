from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Car
from .serializers import CarSerializer, SimpleCarSerializer

# TODO: only show urls to each image when inspecting a car detail page, otherwise - only show the first image?

class CarList(generics.ListAPIView):
    queryset = Car.objects.prefetch_related('images').all()
    serializer_class = SimpleCarSerializer

# Fix this
class CarDetail(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer



# @api_view()
# def car_list(request):
#     queryset = Car.objects.all()
#     serializer = CarSerializer(queryset,many=True)
#     return Response(serializer.data)


# @api_view()
# def car_detail(request, id):
#     car = get_object_or_404(Car,pk=id)
#     serializer = CarSerializer(car)
#     return Response(serializer.data)