from django.db import models

from bvs.abstract.models import AbstractModel, AbstractManager


class PhysiotherapyManager(AbstractManager):
    pass


class Physiotherapy(AbstractModel):
    patient = models.ForeignKey("bvs_patient.Patient", on_delete=models.CASCADE)

    initial_status = models.TextField(null=True)
    applied_methods = models.TextField(null=True)
    dischared_status = models.TextField(null=True)
    observation = models.TextField(null=True)
    current_status = models.TextField(null=True)
    mode_of_followup = models.TextField(null=True)
    followed_by = models.CharField(max_length=100, null=True)

    objects = PhysiotherapyManager()

    def __str__(self):
        return self.patient.registration_number
