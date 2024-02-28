from django.db import models

from bvs.abstract.models import AbstractModel, AbstractManager


class PatientManager(AbstractManager):
    pass


class Patient(AbstractModel):
    creator = models.ForeignKey(to="bvs_user.User", on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now=True)
    fiscal_year = models.CharField(max_length=10, blank=True)
    registration_location = models.CharField(max_length=255, default="KTM")
    registration_number = models.CharField(max_length=20, blank=True, unique=True)

    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255, null=True, blank=True)

    country = models.CharField(max_length=255, null=True, blank=True)
    provence = models.CharField(max_length=255, null=True, blank=True)
    district = models.CharField(max_length=255, null=True, blank=True)
    local = models.CharField(max_length=255, null=True, blank=True)
    ward = models.IntegerField(null=True, blank=True)
    tole = models.CharField(max_length=255, null=True, blank=True)
    foreign_address = models.CharField(max_length=255, null=True, blank=True)

    country2 = models.CharField(max_length=255, null=True, blank=True)
    provence2 = models.CharField(max_length=255, null=True, blank=True)
    district2 = models.CharField(max_length=255, null=True, blank=True)
    local2 = models.CharField(max_length=255, null=True, blank=True)
    ward2 = models.IntegerField(null=True, blank=True)
    tole2 = models.CharField(max_length=255, null=True, blank=True)
    foreign_address2 = models.CharField(max_length=255, null=True, blank=True)

    date_of_birth = models.DateTimeField(null=True, blank=True)
    age_at_incident = models.IntegerField(null=True, blank=True)
    month_at_incident = models.IntegerField(null=True, blank=True)
    day_at_incident = models.IntegerField(null=True, blank=True)
    age_group = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    citizenship_no = models.CharField(max_length=255, null=True, blank=True)
    patient_contact = models.CharField(max_length=15, null=True, blank=True)
    optional_contact = models.CharField(max_length=15, null=True, blank=True)
    parents_contact = models.CharField(max_length=15, null=True, blank=True)
    patient_education = models.ForeignKey(to="bvs_educationlevel.EducationLevel", on_delete=models.CASCADE, null=True,
                                          blank=True)
    # patient_language = models.ForeignKey(to="bvs_language.Language", on_delete=models.CASCADE, null=True, blank=True)
    patient_language = models.ManyToManyField(to="bvs_language.Language", blank=True)

    patient_occupation = models.ForeignKey(to="bvs_occupation.Occupation", related_name='patient_occupation',
                                           on_delete=models.CASCADE, null=True, blank=True)
    suppose_occupation = models.ForeignKey(to="bvs_occupation.Occupation", related_name='suppose_occupation',
                                           on_delete=models.CASCADE, null=True, blank=True)
    parents_occupation = models.ForeignKey(to="bvs_occupation.Occupation", related_name='parents_occupation',
                                           on_delete=models.CASCADE, null=True, blank=True)

    ethnic_group = models.ForeignKey(to="bvs_ethnic.Ethnic", on_delete=models.CASCADE, null=True, blank=True)
    religion = models.ForeignKey(to="bvs_religion.Religion", on_delete=models.CASCADE, null=True, blank=True)
    family_type = models.ForeignKey(to="bvs_family.Family", on_delete=models.CASCADE, null=True, blank=True)

    material_status = models.CharField(max_length=255, null=True, blank=True)
    number_of_child = models.IntegerField(null=True, blank=True)
    number_of_siblings = models.IntegerField(null=True, blank=True)

    economic_status = models.CharField(max_length=150, null=True, blank=True)
    echo_other = models.CharField(max_length=150, null=True, blank=True)
    family_support = models.BooleanField(null=True)
    pregnant_women = models.BooleanField(null=True)
    lactating_mother = models.BooleanField(null=True)
    with_disabilities = models.BooleanField(null=True)
    mental_illness = models.BooleanField(null=True)
    epilepsy = models.BooleanField(null=True)
    hiv_positive = models.BooleanField(null=True)

    date_of_incident = models.DateTimeField(null=True, blank=True)
    area_of_burn = models.TextField(null=True, blank=True)
    percentage_of_burn = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    group_of_percentage = models.CharField(max_length=255, null=True, blank=True)
    degree_of_burn = models.CharField(max_length=255, null=True, blank=True)

    burn_cause = models.ForeignKey(to="bvs_burncause.BurnCause", on_delete=models.CASCADE, null=True, blank=True)
    burn_type = models.ForeignKey(to="bvs_burntype.BurnType", on_delete=models.CASCADE, null=True, blank=True)

    place_of_incident = models.CharField(max_length=255, null=True, blank=True)
    description_of_incident = models.TextField(null=True, blank=True)
    person_at_hospital = models.CharField(max_length=255, null=True, blank=True)
    relation_to_parent = models.CharField(max_length=255, null=True, blank=True)
    person_contact = models.CharField(max_length=50, null=True, blank=True)

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
