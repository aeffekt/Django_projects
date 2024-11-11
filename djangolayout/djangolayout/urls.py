
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from allauth.account.views import login, logout, signup

router = routers.DefaultRouter()    # -->route de model viewset, se registran todos los viewsets
router.register(r'users', user_views.UserViewSet)  


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', include(router.urls)),     # se incluye el router
    path('auth/', include('rest_framework.urls')), # agrega vistas de login en "api-auth/login" y logout
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    path('accounts/', include('allauth.urls')),
    path("login/", login, name="login"),  
    path("logout/", logout, name="logout"), 
    path("signup/", signup, name="signup"), 
]
