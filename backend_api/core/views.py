from django.shortcuts import render
from django.http import HttpResponse


def Bike(request):
    bike = [
        {'brand': 'Ducati', 'model': 'Panigale V4', 'year': 2024},
    ]
    return HttpResponse(bike)