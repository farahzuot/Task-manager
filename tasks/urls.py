from django.urls import path

from tasks.views import ListCreateTaskApi

app_name = 'tasks'
urlpatterns = [
  path('api/tasks/', ListCreateTaskApi.as_view(), name='create-task'),
  # path('api/tasks/{id}', RetrieveTaskApi, name='retrieve-task'),
  # path('api/tasks/{id}', UpdateTaskApi, name='update-task'),
  # path('api/tasks/{id}', DeleteTaskApi, name='delete-task'),
]