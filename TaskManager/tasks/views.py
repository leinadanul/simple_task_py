from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializaer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializaer