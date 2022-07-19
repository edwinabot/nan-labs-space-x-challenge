"""
This module has the admin configurations for this app models
"""

from django.contrib import admin

from trello_integration.models import Bug, Issue, Task

# Register your models here.
admin.site.register(Issue)
admin.site.register(Bug)
admin.site.register(Task)
