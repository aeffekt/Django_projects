from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from to_do import views as to_do
from users import views as users

router = routers.DefaultRouter()
router.register(r'tasks', to_do.TaskViewSet)
router.register(r'users', users.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
