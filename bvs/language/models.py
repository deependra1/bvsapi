from django.db import models

from bvs.abstract.models import AbstractModel, AbstractManager


class LanguageManager(AbstractManager):
    pass


class Language(AbstractModel):
    language_name = models.CharField(max_length=255, null=True)

    objects = LanguageManager()

    def __str__(self):
        return self.language_name
