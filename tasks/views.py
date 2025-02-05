from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from drf_yasg.utils import swagger_auto_schema
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

    @swagger_auto_schema(operation_description="List all tasks.")
    def list(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new task with title and description")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Retrieve a task by its ID")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update an existing task's details")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a task by its ID")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class TaskListView(LoginRequiredMixin, ListView):
    """ List 10 tasks per page. """

    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    """ A view to create a new task. """

    model = Task
    template_name = 'tasks/task_create.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('tasks:tasks-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    template_name = 'tasks/task_update.html'
    context_object_name = 'task'

    def get_success_url(self):
        return reverse_lazy('tasks:tasks-list')

    def get_object(self, queryset=None):
        return get_object_or_404(Task, pk=self.kwargs['id'], user=self.request.user)
