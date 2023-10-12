from django.db import models

from bvs.abstract.models import AbstractModel, AbstractManager


class DonorManager(AbstractManager):
    pass


class Donor(AbstractModel):
    donor_name = models.CharField(max_length=50, null=True)
    donor_address = models.CharField(max_length=100, null=True, blank=True)

    objects = DonorManager()

    def __str__(self):
        return self.donor_name
