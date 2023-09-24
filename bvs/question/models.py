from django.db import models

from bvs.abstract.models import AbstractModel, AbstractManager


class QuestionManager(AbstractManager):
    pass


class Question(AbstractModel):
    questionnaire = models.CharField(max_length=255, null=True, blank=True)

    objects = QuestionManager()

    def __str__(self):
        return self.questionnaire
