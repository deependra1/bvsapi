from django.db import models

from bvs.abstract.models import AbstractModel, AbstractManager


class HospitalManager(AbstractManager):
    pass


class Hospital(AbstractModel):
    hospital_name = models.CharField(max_length=255, null=True)

    objects = HospitalManager()

    def __str__(self):
        return self.hospital_name
