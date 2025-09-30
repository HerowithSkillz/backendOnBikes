# from django.shortcuts import render
# from django.http import JsonResponse
from core.models import Bike
from .serializers import BikeSerializer, EventSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from events.models import Events
from django.http import Http404
from rest_framework import mixins, generics

# Create your views here.
#This by using function based views...
@api_view(['GET', 'POST'])
def bikesView(request):
    if request.method == 'GET':
        #Get all the data from the student table.
        bikes = Bike.objects.all()
        serializer = BikeSerializer(bikes, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def bikeDetailView(request, pk):
    try:
        bike = Bike.objects.get(pk=pk)
    except Bike.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BikeSerializer(bike)
        return Response(serializer.data ,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = BikeSerializer(bike,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        bike.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# class Event(APIView):
#     def get(self, request):
#         events = Events.objects.all()
#         serializer  = EventSerializer(events, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = EventSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class EventDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Events.objects.get(pk=pk)
#         except Events.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk):
#         events = self.get_object(pk)
#         serializer= EventSerializer(events)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         events = self.get_object(pk)
#         serializer = EventSerializer(events, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         events = self.get_object(pk)
#         events.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#Mixinis 
# class Event(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Events.objects.all()
#     serializer_class = EventSerializer

#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)
    
# class EventDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin ,generics.GenericAPIView):
#     queryset= Events.objects.all()
#     serializer_class = EventSerializer

#     def get(self, request, pk):
#         return self.retrieve(request, pk)
    
#     def put(self, request, pk):
#         return self.update(request, pk)
    
#     def delete(self, request, pk):
#         return self.destroy(request, pk)

