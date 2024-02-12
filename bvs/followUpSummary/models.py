from django.db import models

from bvs.abstract.models import AbstractModel, AbstractManager


class FollowUpSummaryManager(AbstractManager):
    pass


class FollowUpSummary(AbstractModel):
    follow_up_summary = models.CharField(max_length=200, null=True)

    objects = FollowUpSummaryManager()

    def __str__(self):
        return self.follow_up_summary
