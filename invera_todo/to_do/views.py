from rest_framework import viewsets, permissions
from .serializer import TaskSerializer, TaskCreateSerializer
from .models import Task
from django.utils.dateparse import parse_date


class TaskViewSet(viewsets.ModelViewSet):    
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filtran las tareas: busqueda, fechas y del usuario autenticado
        query = self.request.GET.get('query') 
        date_str = self.request.GET.get('date') 
        queryset = Task.objects.filter(author=self.request.user)    
        if date_str:
                date = parse_date(date_str)
                if date:
                    queryset = queryset.filter(created__date=date)
        if query:
            queryset = queryset.filter(title__icontains=query)

        return queryset
    
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return TaskCreateSerializer
        return TaskSerializer
    
    def perform_create(self, serializer):
        # Asigna el usuario actual como el autor de la tarea
        serializer.save(author=self.request.user)
