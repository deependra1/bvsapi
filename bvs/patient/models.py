from django.db import models

from bvs.abstract.models import AbstractModel, AbstractManager


class PatientManager(AbstractManager):
    pass


class Patient(AbstractModel):
    creator = models.ForeignKey(to="bvs_user.User", on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now=True)
    fiscal_year = models.CharField(max_length=10, blank=True)
    registration_location = models.CharField(max_length=5, default="KTM")
    registration_number = models.CharField(max_length=20, blank=True, unique=True)

    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255, null=True)

    country = models.CharField(max_length=50, null=True)
    provence = models.CharField(max_length=50, null=True)
    district = models.CharField(max_length=50, null=True)
    local = models.CharField(max_length=50, null=True)
    ward = models.IntegerField(null=True)
    tole = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(null=True)
    age_at_incident = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, null=True)
    citizenship_no = models.CharField(max_length=20, null=True)
    patient_contact = models.CharField(max_length=15, null=True)
    parents_contact = models.CharField(max_length=15, null=True)

    patient_occupation = models.ForeignKey(to="bvs_occupation.Occupation", related_name='patient_occupation', on_delete=models.CASCADE, null=True)
    suppose_occupation = models.ForeignKey(to="bvs_occupation.Occupation", related_name='suppose_occupation', on_delete=models.CASCADE, null=True)
    parents_occupation = models.ForeignKey(to="bvs_occupation.Occupation", related_name='parents_occupation', on_delete=models.CASCADE, null=True)

    ethnic_group = models.ForeignKey(to="bvs_ethnic.Ethnic", on_delete=models.CASCADE, null=True)
    religion = models.ForeignKey(to="bvs_religion.Religion", on_delete=models.CASCADE, null=True)
    family_type = models.ForeignKey(to="bvs_family.Family", on_delete=models.CASCADE, null=True)

    material_status = models.CharField(max_length=50, null=True)
    number_of_child = models.IntegerField(null=True)
    number_of_siblings = models.IntegerField(null=True)
    date_of_incident = models.DateTimeField(null=True)
    area_of_burn = models.CharField(max_length=50, null=True)
    percentage_of_burn = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    degree_of_burn = models.CharField(max_length=50, null=True)
    cause_of_burn = models.CharField(max_length=50, null=True)
    type_of_burn = models.CharField(max_length=50, null=True)
    place_of_incident = models.CharField(max_length=50, null=True)
    description_of_incident = models.TextField(null=True)

    objects = PatientManager()

    # def __str__(self):
    #     return self.fname

    def __str__(self):
        return self.registration_number

    def save(self, *args, **kwargs):
        if not self.registration_number:
            last_registration = Patient.objects.filter(
                fiscal_year=self.fiscal_year,
                registration_location=self.registration_location
            ).order_by('-registration_number').first()

            if last_registration:
                last_serial_number = int(last_registration.registration_number.split('-')[-1])
                new_serial_number = last_serial_number + 1
            else:
                new_serial_number = 1

            self.registration_number = f"{self.fiscal_year}-{self.registration_location}-{new_serial_number}"

        super().save(*args, **kwargs)
