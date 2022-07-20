from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from trello_integration.models import Bug


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
        self.assertTrue(Bug.objects.filter(description=description).exists())

    def test_bug_request_missing_description(self):
        """
        Testing with a missing attribute, in this case, the description
        """
        payload = {
            "type": "bug",
        }
        response = self.client.post(self.path, payload, format="json")
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
