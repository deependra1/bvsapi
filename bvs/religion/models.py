from django.db import models

from bvs.abstract.models import AbstractModel, AbstractManager


class ReligionManager(AbstractManager):
    pass


class Religion(AbstractModel):
    religion = models.CharField(max_length=255, null=True)

    objects = ReligionManager()

    def __str__(self):
        return self.religion
