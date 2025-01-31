from django.test import TestCase
from django.urls import reverse

from to_do_app.forms import TagForm


class TaskViewTests(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "to_do_app/home.html")

    def test_task_creation_view(self):
        response = self.client.get(reverse("task-create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "to_do_app/task_form.html")

class TagFormTests(TestCase):
    def test_valid_tag_form(self):
        form_data = {"name": "Test Tag"}
        form = TagForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_tag_form(self):
        form_data = {"name": ""}
        form = TagForm(data=form_data)
        self.assertFalse(form.is_valid())