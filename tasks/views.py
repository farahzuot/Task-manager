from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import IsAuthenticated

from tasks.models import Task
from tasks.permissions import IsTaskOwner
from tasks.serializers import TaskSerializer


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    """
    A viewset for managing tasks.

    Allows users to:
    - List, create, retrieve, update, and delete their tasks.

    Permissions:
    - Authenticated users can access their tasks only.
    """
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsTaskOwner)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)





