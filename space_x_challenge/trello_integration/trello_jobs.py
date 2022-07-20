from typing import Union

import django_rq

from trello_integration.models import Bug, Task, Issue


class TrelloJobs:
    default_queue = django_rq.get_queue("default")

    def create_trello_card(self, instance: Union[Bug, Task, Issue]):
        self.default_queue.enqueue(send_card, instance=instance)

def send_card(instance):
    print(instance)
    raise NotImplementedError
