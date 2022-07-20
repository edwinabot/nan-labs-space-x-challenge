from rest_framework.serializers import ModelSerializer

from trello_integration.models import Bug, Issue, Task


class BugSerializer(ModelSerializer):
    class Meta:
        model = Bug
        fields = ["id", "title", "description"]


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ["id", "title", "description"]


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "category"]
