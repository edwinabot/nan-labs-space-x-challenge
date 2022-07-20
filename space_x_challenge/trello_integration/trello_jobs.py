import random
from dataclasses import dataclass
from typing import Union


import django_rq
import requests

from trello_integration.models import Bug, Task, Issue
from space_x_challenge.settings import TRELLO_CONF


class TrelloJobs:
    default_queue = django_rq.get_queue("default")

    def create_trello_card(self, instance: Union[Bug, Task, Issue]):
        handler = self._get_task_handler(type(instance))
        self.default_queue.enqueue(
            handler, trello_client_conf=TRELLO_CONF, instance=instance
        )

    def _get_task_handler(self, issue_type):
        """
        Returns the right handler for an issue type
        """
        return {
            Bug: send_bug,
            Task: send_task,
            Issue: send_issue,
        }[issue_type]


@dataclass
class TrelloConf:
    key: str
    token: str
    board_id: str
    todo_list_id: str
    research_label_id: str
    test_label_id: str
    maintenance_label_id: str
    bug_label_id: str


class TrelloClient:
    def __init__(self, trello_conf: TrelloConf) -> None:
        self.conf = trello_conf
        self.api_url = "https://api.trello.com"
        self.cards_path = "/1/cards"
        self.boards_path = "/1/boards/"
        self.query_args = {"key": trello_conf.key, "token": trello_conf.token}

    def get_board_members(self):
        response: requests.Response = requests.get(
            f"{self.api_url}{self.boards_path}/{self.conf.board_id}/members",
            params=self.query_args,
        )
        response.raise_for_status()
        data = response.json()
        return data

    def post_card(self, payload):
        response: requests.Response = requests.post(
            self.api_url + "/1/cards", json=payload, params=self.query_args
        )
        response.raise_for_status()
        return response.json()


def send_bug(trello_client_conf: dict, instance: Bug):
    client = TrelloClient(TrelloConf(**trello_client_conf))
    members = client.get_board_members()
    random_member = random.choices(members)[0]
    payload = {
        "name": instance.title,
        "desc": instance.description,
        "idList": client.conf.todo_list_id,
        "pos": "top",
        "idMembers": [
            random_member["id"],
        ],
        "idLabels": [
            client.conf.bug_label_id,
        ],
    }
    result = client.post_card(payload)
    print(f'Created Bug {result["shortUrl"]}')


def send_issue(trello_client_conf: dict, instance: Issue):
    client = TrelloClient(TrelloConf(**trello_client_conf))
    payload = {
        "name": instance.title,
        "desc": instance.description,
        "idList": client.conf.todo_list_id,
        "pos": "top",
    }
    result = client.post_card(payload)
    print(f'Created Issue {result["shortUrl"]}')


def send_task(trello_client_conf: dict, instance: Task):
    raise NotImplementedError
