import pytest
from rest_framework import status
from django.urls import reverse


@pytest.mark.django_db
def test_create_task_unauthenticated(api_client):
    """
    Test case when the user is not authenticated and tries to create a task.
    """
    data = {
        "title": "New Task",
        "description": "This is a new task.",
    }
    url = reverse("tasks:task-list")
    response = api_client.post(url, data, format="json")
    assert response.status_code == 403


@pytest.mark.django_db
def test_create_task_authenticated(api_client, user):
    """
    Test case when the user is authenticated and successfully creates a task.
    """
    api_client.force_authenticate(user=user)
    data = {
        "title": "New Task",
        "description": "This is a new task.",
    }
    url = reverse("tasks:task-list")
    response = api_client.post(url, data, format="json")
    assert response.status_code == 201
    assert response.data["title"] == data["title"]
    assert response.data["description"] == data["description"]
    assert response.data["user"] == "testuser"


@pytest.mark.django_db
def test_create_task_invalid_data(api_client, user):
    """
    Test case when the user submits invalid data to create a task - missing title.
    """
    api_client.force_authenticate(user=user)
    data = {
        "description": "This task has no title.",
    }
    url = reverse("tasks:task-list")
    response = api_client.post(url, data, format="json")
    assert response.status_code == 400
