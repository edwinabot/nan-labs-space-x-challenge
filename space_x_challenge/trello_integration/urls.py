from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from trello_integration.views import IssueDispatcherView

urlpatterns = [
    path("issues/", IssueDispatcherView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
