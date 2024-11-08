from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()    # -->route de model viewset, se registran todos los viewsets
router.register(r'tasks', views.TaskViewSet)  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),     # se incluye el router
    path('api_auth/', include('rest_framework.urls')),
    #path('api/', include('api.urls')), #--> route de model view
]
