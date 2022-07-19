import random, string

from django.db import models


class Task(models.Model):
    CATEGORIES = (("MA", "Maintenance"), ("RE", "Research"), ("TE", "Test"))

    title = models.CharField(max_length=144)
    category = models.CharField(choices=CATEGORIES, max_length=2)


class Issue(models.Model):
    title = models.CharField(max_length=144)
    description = models.TextField()


def make_bug_title(
    word_chars=string.ascii_letters,
    number_chars=string.digits,
    word_length=8,
    numbers_length=8,
) -> str:
    """
    Returns a randomized string with the following pattern: bug-{word}-{number}
    """
    word = "".join(random.choice(word_chars) for i in range(word_length))
    number = "".join(random.choice(number_chars) for i in range(numbers_length))
    return f"bug-{word}-{number}"


class Bug(models.Model):
    title = models.CharField(default=make_bug_title, max_length=144)
    description = models.TextField()
