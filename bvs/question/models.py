from django.db import models

from bvs.abstract.models import AbstractModel, AbstractManager


class QuestionManager(AbstractManager):
    pass


class Question(AbstractModel):
    questionnaire = models.TextField(null=True, blank=True)

    objects = QuestionManager()

    def __str__(self):
        return self.questionnaire
