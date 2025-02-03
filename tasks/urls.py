from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasks.views import TaskViewSet, TaskListView, TaskCreateView, TaskUpdateView

app_name = 'tasks'
router = DefaultRouter()
router.register(r'api/tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/', TaskListView.as_view(), name='tasks-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='add-task'),
    path('tasks/<int:id>/', TaskUpdateView.as_view(), name='task-details'),
]