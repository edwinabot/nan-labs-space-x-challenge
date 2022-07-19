import re

from django.test import TestCase

from trello_integration.models import Bug

# Create your tests here.
class BugTestCase(TestCase):
    def setUp(self) -> None:
        expected_description = "A very detailed explanation of the bug"
        Bug.objects.create(description=expected_description)

    def test_there_is_a_bug(self):
        bug_count = Bug.objects.count()
        self.assertGreaterEqual(1, bug_count)

    def test_that_the_bug_has_randomized_title(self):
        title_regex = r"(bug)-(\w+)-(\d+)"
        bug = Bug.objects.first()
        matches = re.findall(title_regex, bug.title)[0]
        self.assertEqual(3, len(matches))
        self.assertEqual("bug", matches[0])
        self.assertIsInstance(int(matches[2]), int)
