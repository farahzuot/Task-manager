import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from tasks.models import Task

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser", password="testpass")

@pytest.fixture
def second_user(db):
    return User.objects.create_user(username="testuser2", password="testpass2")

@pytest.fixture
def task(db, user):
    return Task.objects.create(title="Task 1", description="Task 1 description.", user=user)