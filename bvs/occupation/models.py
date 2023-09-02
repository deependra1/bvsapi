from django.db import models

from bvs.abstract.models import AbstractModel, AbstractManager


class OccupationManager(AbstractManager):
    pass


class Occupation(AbstractModel):
    occupation_name = models.CharField(max_length=50, null=True)

    objects = OccupationManager()

    def __str__(self):
        return self.occupation_name
