from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasks.views import TaskViewSet


app_name = 'tasks'
router = DefaultRouter()
router.register(r'api/tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]