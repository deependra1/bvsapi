from django.db import models

from bvs.abstract.models import AbstractModel, AbstractManager


class BurnCauseManager(AbstractManager):
    pass


class BurnCause(AbstractModel):
    burn_cause = models.CharField(max_length=255, null=True)

    objects = BurnCauseManager()

    def __str__(self):
        return self.burn_cause

