from django.db import models

from bvs.abstract.models import AbstractModel, AbstractManager


class BurnTypeManager(AbstractManager):
    pass


class BurnType(AbstractModel):
    burn_type = models.CharField(max_length=200, null=True)

    objects = BurnTypeManager()

    def __str__(self):
        return self.burn_type

