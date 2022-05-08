from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list),
    path('<int:id>/', views.car_detail),    
]
