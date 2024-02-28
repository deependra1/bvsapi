from django.db import models

from bvs.abstract.models import AbstractModel, AbstractManager


class PhysiotherapyManager(AbstractManager):
    pass


class Physiotherapy(AbstractModel):
    patient = models.ForeignKey("bvs_patient.Patient", on_delete=models.CASCADE)

    initial_status = models.TextField(null=True, blank=True)
    applied_methods = models.TextField(null=True, blank=True)
    dischared_status = models.TextField(null=True, blank=True)
    observation = models.TextField(null=True, blank=True)
    current_status = models.TextField(null=True, blank=True)
    mode_of_followup = models.TextField(null=True, blank=True)
    followed_by = models.CharField(max_length=255, null=True, blank=True)
    followup_summary = models.ForeignKey(to="bvs_followUpSummary.FollowUpSummary", on_delete=models.CASCADE, null=True, blank=True)
    number_of_session = models.IntegerField(null=True, blank=True)


    objects = PhysiotherapyManager()

    def __str__(self):
        return self.patient.registration_number
