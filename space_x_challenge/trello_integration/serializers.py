from rest_framework.serializers import ModelSerializer

from trello_integration.models import Bug


class BugSerializer(ModelSerializer):
    class Meta:
        model = Bug
        fields = ["id", "title", "description"]
