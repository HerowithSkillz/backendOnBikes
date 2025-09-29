from django.urls import path
from . import views

urlpatterns = [
    path('', views.Bike, name='bike'),
]
