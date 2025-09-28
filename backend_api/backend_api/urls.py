from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    #Web Application Endpoints
    path('core/', include('core.urls')),



    #APi ENdpoints
    path('api/v1/', include('api.urls'))
]
