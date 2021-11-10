from django.urls import path
from HealthyPillApp import views



urlpatterns = [

    path('', views.base, name="base"),
    path('calendario/', views.calendario, name="calendario"),
    
]
