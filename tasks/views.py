from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView
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


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tasks/task_create.html'
    fields = ['title', 'description', 'due_date']
    success_url = reverse_lazy('tasks:tasks-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def get_object(self):
        # Ensures the task ID is used to retrieve the correct task
        task_id = self.kwargs['id']
        return Task.objects.get(id=task_id, user=self.request.user)


class TaskUpdateStatusView(View):
    def patch(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'], user=request.user)
        task.completed = not task.completed
        task.save()

        return JsonResponse({'completed': task.completed})