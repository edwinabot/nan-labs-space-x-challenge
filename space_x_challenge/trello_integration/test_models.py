import re

from django.test import TestCase

from trello_integration.models import Bug, Issue, Task

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


class IssueTestCase(TestCase):
    def setUp(self) -> None:
        Issue.objects.create(
            title="As an Cosmonaut, I need to know my location within the Solar System",
            description="There is a need to know where we are flying within the solar system, having the sun as a point of reference",
        )

    def test_there_is_an_issue(self) -> None:
        issue_count = Issue.objects.count()
        self.assertGreaterEqual(1, issue_count)


class TaskTestCase(TestCase):
    def setUp(self) -> None:
        Task.objects.create(
            title="Ensure rubber junctures are OK, don't repeate the Challenger experience",
            category=Task.TaskCategories.MAINTENANCE,
        )

    def test_there_is_a_task(self):
        task_count = Task.objects.count()
        self.assertGreaterEqual(1, task_count)
