from django.db import models

from bvs.abstract.models import AbstractModel, AbstractManager


class EthnicManager(AbstractManager):
    pass


class Ethnic(AbstractModel):
    ethnic_group = models.CharField(max_length=255, null=True)

    objects = EthnicManager()

    def __str__(self):
        return self.ethnic_group
