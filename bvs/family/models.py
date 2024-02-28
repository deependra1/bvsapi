from django.db import models

from bvs.abstract.models import AbstractModel, AbstractManager


class FamilyManager(AbstractManager):
    pass


class Family(AbstractModel):
    family_type = models.CharField(max_length=255, null=True)

    objects = FamilyManager()

    def __str__(self):
        return self.family_type
