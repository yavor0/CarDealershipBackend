from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import Car, CarEvaluation
from .serializers import CarSerializer, SimpleCarSerializer, CarEvaluationSerializer
from django.core.mail import send_mail
# TODO: only show urls to each image when inspecting a car detail page, otherwise - only show the first image?

class CarList(generics.ListAPIView):
    queryset = Car.objects.prefetch_related('images').all()
    serializer_class = SimpleCarSerializer


class CarDetail(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

# def notify_owner(data):
#     send_mail(f'test email{0}', 'hello world', 'devemail500@gmail.com', ['targer'])


class CarEvaluate(generics.CreateAPIView):
    serializer_class = CarEvaluationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # notify_owner(request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

