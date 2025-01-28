from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated

from tasks.models import Task
from tasks.serializers import TaskSerializer


# Create your views here.
class ListCreateTaskApi(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)