from django.urls import path
from . import views

urlpatterns = [
    path('bikes/', views.bikesView),
    path('bikes/<int:pk>/', views.bikeDetailView )
]
#video timestamp: 36:47
