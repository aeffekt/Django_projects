
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from rest_framework import routers

router = routers.DefaultRouter()    # -->route de model viewset, se registran todos los viewsets
router.register(r'users', user_views.UserViewSet)  


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', include(router.urls)),     # se incluye el router
    path('auth/', include('rest_framework.urls')), # agrega vistas de login en "api-auth/login" y logout
]
