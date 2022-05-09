from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.car_list),
    path('cars/<int:id>/', views.car_detail)  
]
