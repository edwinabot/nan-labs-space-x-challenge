# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class IssueDispatcherView(APIView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        """
        This view processes, stores and dispatches the right kind of issue to the
        trello worker
        """
        return Response("Not Implemented", status=status.HTTP_501_NOT_IMPLEMENTED)
