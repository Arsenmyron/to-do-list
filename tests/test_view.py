from django.test import TestCase
from django.urls import reverse

from to_do_app.models import Task


class TaskStatusToggleTests(TestCase):
    def test_toggle_task_status(self):
        task = Task.objects.create(content="Test Task", is_done=False)
        response = self.client.post(reverse("task-toggle-status", args=[task.id]))
        task.refresh_from_db()
        self.assertTrue(task.is_done)