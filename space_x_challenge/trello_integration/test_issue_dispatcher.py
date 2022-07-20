from unittest.mock import patch

import fakeredis
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from trello_integration.models import Bug, Issue, Task


@patch(
    "trello_integration.views.IssueDispatcherView.trello_jobs.default_queue.connection",
    fakeredis.FakeStrictRedis(),
)
class BugsTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.path = "/api/issues/"

    def test_valid_bug_request(self):
        """
        Testing with a valid bug request.
        """
        description = "Houston... we have a problem"
        payload = {"type": "bug", "description": description}
        response = self.client.post(self.path, payload, format="json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(description, response.data["description"])
        self.assertTrue(
            Bug.objects.filter(description=response.data["description"]).exists()
        )

    def test_bug_request_missing_description(self):
        """
        Testing with a missing attribute, in this case, the description
        """
        payload = {
            "type": "bug",
        }
        response = self.client.post(self.path, payload, format="json")
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)


@patch(
    "trello_integration.views.IssueDispatcherView.trello_jobs.default_queue.connection",
    fakeredis.FakeStrictRedis(),
)
class IssuesTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.path = "/api/issues/"
        self.issue_type = "issue"

    def test_valid_issue_request(self):
        """
        Testing with a valid Issue request.
        """
        description = (
            "There's so much I should write here, but I don't have the time for that"
        )
        title = "The best Issue title you've ever seen"
        payload = {"type": self.issue_type, "title": title, "description": description}
        response = self.client.post(self.path, payload, format="json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertTrue(Issue.objects.filter(title=response.data["title"]).exists())

    def test_issue_request_missing_title(self):
        """
        Testing with a missing attribute, in this case, the description
        """
        payload = {"type": self.issue_type, "description": "Some description over here"}
        response = self.client.post(self.path, payload, format="json")
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)


@patch(
    "trello_integration.views.IssueDispatcherView.trello_jobs.default_queue.connection",
    fakeredis.FakeStrictRedis(),
)
class TaskTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.path = "/api/issues/"
        self.issue_type = "task"

    def test_maintenance_task_request(self):
        """
        Testing for maintenance
        """
        title = "You go and build a damn rocket"
        task_category = "Maintenance"
        payload = {"type": self.issue_type, "title": title, "category": task_category}
        response = self.client.post(self.path, payload, format="json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertTrue(Task.objects.filter(title=response.data["title"]).exists())

    def test_research_task_request(self):
        """
        Testing for maintenance
        """
        title = "Try to buy Twitter and cause mayhem"
        task_category = "Research"
        payload = {"type": self.issue_type, "title": title, "category": task_category}
        response = self.client.post(self.path, payload, format="json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertTrue(Task.objects.filter(title=response.data["title"]).exists())

    def test_test_task_request(self):
        """
        Testing for maintenance
        """
        title = "Try to land a rocket in a tiny platform in the ocean"
        task_category = "Test"
        payload = {"type": self.issue_type, "title": title, "category": task_category}
        response = self.client.post(self.path, payload, format="json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertTrue(Task.objects.filter(title=response.data["title"]).exists())

    def test_issue_request_missing_title(self):
        """
        Testing with a missing attribute, in this case, the description
        """
        payload = {
            "type": self.issue_type,
        }
        response = self.client.post(self.path, payload, format="json")
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
