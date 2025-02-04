import pytest
from django.urls import reverse, path


@pytest.mark.django_db
def test_retrieve_task_not_authenticated(api_client, task):
    """
    Test case when the user is not authenticated.
    """
    url = reverse("tasks:task-detail", kwargs={"pk": task.pk})
    response = api_client.get(url)
    assert response.status_code == 403
    assert response.data["detail"] == "Authentication credentials were not provided."


@pytest.mark.django_db
def test_retrieve_task_authenticated_not_owner(api_client, second_user, task):
    """
    Test case when the user is authenticated but not the owner of the task.
    """
    api_client.force_authenticate(second_user)
    url = reverse('tasks:task-detail', kwargs={'pk': task.pk})
    response = api_client.get(url)
    assert response.status_code == 404


@pytest.mark.django_db
def test_retrieve_task_for_owner_user(api_client, user, task):
    """
    Test case when the user is owner of the task.
    """
    api_client.force_authenticate(user)
    url = reverse('tasks:task-detail', kwargs={'pk': task.pk})
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data['title'] == task.title
    assert response.data['description'] == task.description


@pytest.mark.django_db
def test_retrieve_task_not_found(api_client, user):
    """
    Test case when the task does not exist.
    """
    api_client.force_authenticate(user=user)
    url = reverse("tasks:task-detail", kwargs={"pk": 9999})
    response = api_client.get(url)
    assert response.status_code == 404
    assert response.data["detail"] == 'No Task matches the given query.'