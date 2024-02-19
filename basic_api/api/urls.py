'''from django.urls import path
from .views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-retrieve-update-destroy'),
]
CON VIEWSETS Y ROUTER ESTE ARCHIVO NO HACE FALTA!!!!!!!!    '''