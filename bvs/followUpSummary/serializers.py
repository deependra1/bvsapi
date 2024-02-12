from bvs.abstract.serializers import AbstractSerializer
from bvs.followUpSummary.models import FollowUpSummary


class FollowUpSummarySerializer(AbstractSerializer):
    class Meta:
        model = FollowUpSummary
        fields = [
            "id",
            "follow_up_summary",
            "created",
            "updated",
        ]

