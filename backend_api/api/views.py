from django.shortcuts import render
from django.http import JsonResponse
from core.models import Bike


# Create your views here.
def bikesView(request):
    bikes = Bike.objects.all()
    bikes_list = list(bikes.values())
    return JsonResponse(bikes_list, safe=False)