from django.db import models

from bvs.abstract.models import AbstractModel, AbstractManager


class PsychosocialManager(AbstractManager):
    pass


class Psychosocial(AbstractModel):
    patient = models.ForeignKey("bvs_patient.Patient", on_delete=models.CASCADE)

    client_history = models.TextField(null=True)
    client_complain = models.TextField(null=True)
    intervention = models.TextField(null=True)
    changes_after_intervention = models.TextField(null=True)
    detailed_followup_report = models.TextField(null=True)
    followup_summary = models.TextField(null=True)
    mode_of_followup = models.TextField(null=True)
    followed_by = models.CharField(max_length=100, null=True)

    objects = PsychosocialManager()

    def __str__(self):
        return self.patient.registration_number
