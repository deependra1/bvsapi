from django.db import models

from bvs.abstract.models import AbstractModel, AbstractManager


class PsychosocialManager(AbstractManager):
    pass


class Psychosocial(AbstractModel):
    patient = models.ForeignKey("bvs_patient.Patient", on_delete=models.CASCADE)

    client_history = models.TextField(null=True, blank=True)
    client_complain = models.TextField(null=True, blank=True)
    intervention = models.TextField(null=True, blank=True)
    changes_after_intervention = models.TextField(null=True, blank=True)
    detailed_followup_report = models.TextField(null=True, blank=True)
    followup_summary = models.ForeignKey(to="bvs_followUpSummary.FollowUpSummary", on_delete=models.CASCADE, null=True, blank=True)
    mode_of_followup = models.TextField(null=True, blank=True)
    followed_by = models.CharField(max_length=255, null=True, blank=True)
    number_of_counseling = models.IntegerField(null=True, blank=True)

    objects = PsychosocialManager()

    def __str__(self):
        return self.patient.registration_number
