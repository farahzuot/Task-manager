from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasks.views import TaskViewSet, TaskListView, TaskCreateView, TaskDetailView, TaskUpdateStatusView

app_name = 'tasks'
router = DefaultRouter()
router.register(r'api/tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/', TaskListView.as_view(), name='tasks-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='add-task'),
    path('tasks/<int:id>/', TaskDetailView.as_view(), name='task-details'),
    path('tasks/<int:pk>/update-status/', TaskUpdateStatusView.as_view(), name='task-update-status'),

]