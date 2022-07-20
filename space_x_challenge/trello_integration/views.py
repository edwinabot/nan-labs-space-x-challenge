# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from trello_integration.models import Bug
from trello_integration.serializers import BugSerializer

class IssueDispatcherView(APIView):
    type_bug = "bug"
    type_task = "task"
    type_issue = "issue"

    def post(self, request: Request, *args, **kwargs) -> Response:
        """
        This view processes, stores and dispatches the right kind of issue to the
        trello worker
        """
        requested_type = request.data.pop("type")
        issue_handler = self.get_issue_handler(requested_type)
        result = issue_handler(request.data)
        return result

    def get_issue_handler(self, issue_type):
        """
        Returns the right handler for an issue type
        """
        return {
            self.type_bug: self.handle_bug,
            self.type_task: self.handle_task,
            self.type_issue: self.handle_issue,
        }[issue_type]

    def handle_bug(self, payload):
        """
        This method processes Bug requests
        """
        bug_serializer = BugSerializer(data=payload)
        if bug_serializer.is_valid():
            bug_serializer.save()
            return Response(bug_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(bug_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def handle_issue(self, payload):
        return Response("Not Implemented", status=status.HTTP_501_NOT_IMPLEMENTED)

    def handle_task(self, payload):
        return Response("Not Implemented", status=status.HTTP_501_NOT_IMPLEMENTED)
