from django.db import models

from bvs.abstract.models import AbstractModel, AbstractManager


class TreatmentManager(AbstractManager):
    pass


class Treatment(AbstractModel):
    patient = models.ForeignKey("bvs_patient.Patient", on_delete=models.CASCADE)

    hospital = models.CharField(max_length=50, null=True)
    hospitalized_date = models.DateTimeField(null=True)
    doctor_name = models.CharField(max_length=50, null=True)
    dischared_date = models.DateTimeField(null=True)
    expired_date = models.DateTimeField(null=True)
    current_status = models.CharField(max_length=50, null=True)

    objects = TreatmentManager()

    def __str__(self):
        return self.hospital
