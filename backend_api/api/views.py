from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def bikesView(request):
    bikes = {
        'brand': 'HONDA',
        'name': 'CBR 1000RR',
        'year': 2025
    }
    return JsonResponse(bikes)