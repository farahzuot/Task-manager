from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tasks.models import Task
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Create Superuser
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "admin123")
            self.stdout.write(self.style.SUCCESS("Superuser created."))

        # Create a Regular User
        user, created = User.objects.get_or_create(username="user", defaults={"email": "user@example.com"})
        if created:
            user.set_password("user123")
            user.save()
            self.stdout.write(self.style.SUCCESS("Regular user created."))

        # Create 10 Tasks
        for i in range(1, 11):
            Task.objects.create(
                title=f"Task {i}",
                description=f"Lorem Ipsum is simply dummy text of the printing and typesetting industry."
                            f" Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,"
                            f" when an unknown printer took a galley of type and scrambled it to make a type specimen book."
                            f" It has survived not only five centuries, but also the leap into electronic typesetting,"
                            f" remaining essentially unchanged.",
                completed=random.choice([True, False]),
                user=user
            )

        self.stdout.write(self.style.SUCCESS("10 Tasks created successfully!"))
