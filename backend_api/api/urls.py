from django.urls import path
from . import views

urlpatterns = [
    path('bikes/', views.bikesView),
    path('bikes/<int:pk>/', views.bikeDetailView ),

    path('events/', views.Event.as_view()),
    path('events/<int:pk>/', views.EventDetail.as_view()),
]
#video timestamp: 36:47
