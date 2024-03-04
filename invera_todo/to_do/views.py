from rest_framework import viewsets, permissions
from .serializer import TaskSerializer, TaskCreateSerializer
from .models import Task


class TaskViewSet(viewsets.ModelViewSet):    
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filtrar las tareas del usuario actual
        return Task.objects.filter(author=self.request.user)
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return TaskCreateSerializer
        return TaskSerializer
    
    def perform_create(self, serializer):
        # Asigna el usuario actual como el autor de la tarea
        serializer.save(author=self.request.user)
