from django.db import models

from bvs.abstract.models import AbstractModel, AbstractManager


class EducationLevelManager(AbstractManager):
    pass


class EducationLevel(AbstractModel):
    education_level = models.CharField(max_length=50, null=True)

    objects = EducationLevelManager()

    def __str__(self):
        return self.education_level
