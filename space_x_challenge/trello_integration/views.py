# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from trello_integration.trello_jobs import TrelloJobs
from trello_integration.serializers import (
    BugSerializer,
    IssueSerializer,
    TaskSerializer,
)


class IssueDispatcherView(APIView):
    type_bug = "bug"
    type_task = "task"
    type_issue = "issue"
    trello_jobs = TrelloJobs()

    def post(self, request: Request, *args, **kwargs) -> Response:
        """
        This view processes, stores and dispatches the right kind of issue to the
        trello worker
        """
        requested_type = request.data.pop("type")
        serializer = self.get_issue_serializer(requested_type)
        response, instance = self.handle_payload(request.data, serializer)
        if instance is not None:
            self.trello_jobs.create_trello_card(instance)
        return response

    def get_issue_serializer(self, issue_type):
        """
        Returns the right Serializer for an issue type
        """
        return {
            self.type_bug: BugSerializer,
            self.type_task: TaskSerializer,
            self.type_issue: IssueSerializer,
        }[issue_type]

    def handle_payload(self, payload, serializer):
        """
        This method processes Bug requests. If the payload is valid
        it will return a 201 response and the created instance,
        else it will return a 400 response and None
        """
        bug_serializer = serializer(data=payload)
        if bug_serializer.is_valid():
            bug_serializer.save()
            return (
                Response(bug_serializer.data, status=status.HTTP_201_CREATED),
                bug_serializer.instance,
            )
        return (
            Response(bug_serializer.errors, status=status.HTTP_400_BAD_REQUEST),
            None,
        )
