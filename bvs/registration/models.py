from django.db import models
from bvs.abstract.models import AbstractModel, AbstractManager


class RegistrationManager(AbstractManager):
    pass


class Registration(AbstractModel):
    registration_date = models.DateField()
    fiscal_year = models.CharField(max_length=10, blank=True)
    registration_location = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=20, blank=True, unique=True)

    objects = RegistrationManager()

    def __str__(self):
        return f"Registration {self.registration_number}"

    def save(self, *args, **kwargs):
        if not self.registration_number:
            last_registration = Registration.objects.filter(
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
