from django.db import models
from bvs.abstract.models import AbstractModel, AbstractManager


class FundingManager(AbstractManager):
    pass


class Funding(AbstractModel):
    patient = models.ForeignKey("bvs_patient.Patient", on_delete=models.CASCADE)

    donor = models.ForeignKey("bvs_donor.Donor", on_delete=models.CASCADE, null=True, blank=True)
    service_title = models.CharField(max_length=200, null=True, blank=True)
    funding_amount = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)

    objects = FundingManager()

    def __str__(self):
        return self.donor.donor_name
