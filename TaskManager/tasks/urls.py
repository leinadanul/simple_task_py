from django.urls import path
from . import views

urlpatterns = [
        path('tasks/', views.task_list, name='task_list'),
        path('tasks/task/new/', views.task_create, name='task_create'),  # Define la URL para crear tarea
        path('tasks/task/<int:pk>/', views.task_detail, name='task_detail'),
        path('tasks/task/<int:pk>/update/', views.task_update, name='task_update'),  # Define la URL para actualizar la tarea
        path('tasks/task/<int:pk>/delete/', views.task_delete, name='task_delete'),  # Define la URL para eliminar la tarea


        # Otras rutas...
]