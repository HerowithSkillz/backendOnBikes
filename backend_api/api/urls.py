from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('events', views.EventViewset, basename='event')

urlpatterns = [
    path('bikes/', views.bikesView),
    path('bikes/<int:pk>/', views.bikeDetailView ),

    # path('events/', views.Event.as_view()),
    # path('events/<int:pk>/', views.EventDetail.as_view()),
    path('', include(router.urls))
]
#video timestamp: 36:47
