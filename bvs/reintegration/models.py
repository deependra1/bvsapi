from django.db import models
from bvs.abstract.models import AbstractModel, AbstractManager


class ReintegrationManager(AbstractManager):
    pass


class Reintegration(AbstractModel):
    patient = models.ForeignKey("bvs_patient.Patient", on_delete=models.CASCADE)

    question = models.ForeignKey("bvs_question.Question", on_delete=models.CASCADE, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)

    objects = ReintegrationManager()

    def __str__(self):
        return self.question.questionnaire
