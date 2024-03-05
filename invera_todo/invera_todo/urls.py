from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from to_do import views as to_do
from users import views as users


router = routers.DefaultRouter()
router.register(r'tasks', to_do.TaskViewSet, basename='task')   # se define el basename, por usar: def get_queryset
router.register(r'users', users.UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
