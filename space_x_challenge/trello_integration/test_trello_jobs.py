from django.test import TestCase

from trello_integration.models import Bug, Issue, Task
from trello_integration.trello_jobs import send_bug, send_issue, send_task
from space_x_challenge.settings import TRELLO_CONF


class TestBugs(TestCase):
    def setUp(self) -> None:
        self.bug = Bug.objects.create(description="A nasty bug somewhere")

    def test_send_bug(self):
        send_bug(TRELLO_CONF, self.bug)


class TestIssues(TestCase):
    def setUp(self) -> None:
        self.issue = Issue.objects.create(
            description="An issue that needs to be tackled", title="A meaningful tittle"
        )

    def test_send_issue(self):
        send_issue(TRELLO_CONF, self.issue)


class TestTasks(TestCase):
    def setUp(self) -> None:
        self.research_task = Task.objects.create(
            title="A research task", category=Task.TaskCategories.RESEARCH
        )
        self.maintenance_task = Task.objects.create(
            title="A maintenance tittle", category=Task.TaskCategories.MAINTENANCE
        )
        self.test_task = Task.objects.create(
            title="A test tittle", category=Task.TaskCategories.TEST
        )

    def test_send_maintenance(self):
        send_task(TRELLO_CONF, self.maintenance_task)

    def test_send_research(self):
        send_task(TRELLO_CONF, self.research_task)

    def test_send_test(self):
        send_task(TRELLO_CONF, self.test_task)
