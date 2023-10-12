from django.db import models

from bvs.abstract.models import AbstractModel, AbstractManager


class TreatmentManager(AbstractManager):
    pass


class Treatment(AbstractModel):
    patient = models.ForeignKey("bvs_patient.Patient", on_delete=models.CASCADE)
    # for transport
    mode_of_transport = models.CharField(max_length=50, null=True)
    distance = models.IntegerField(null=True, blank=True)
    time = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    duration_of_stay = models.IntegerField(null=True, blank=True)

    hospital = models.CharField(max_length=200, null=True, blank=True)
    hospitalized_date = models.DateTimeField(null=True, blank=True)
    doctor_name = models.CharField(max_length=150, null=True, blank=True)
    dischared_date = models.DateTimeField(null=True, blank=True)
    expired_date = models.DateTimeField(null=True, blank=True)
    # current_status = models.CharField(max_length=50, null=True)

    no_of_surgery = models.IntegerField(null=True, blank=True)
    no_of_skin_graft = models.IntegerField(null=True, blank=True)
    no_of_debridement = models.IntegerField(null=True, blank=True)
    no_of_amputation = models.IntegerField(null=True, blank=True)
    no_of_dressing = models.IntegerField(null=True, blank=True)
    no_of_nutritional = models.IntegerField(null=True, blank=True)
    medical_support = models.IntegerField(null=True, blank=True)
    is_post_treatment = models.BooleanField(null=True)

    objects = TreatmentManager()

    def __str__(self):
        return self.hospital
