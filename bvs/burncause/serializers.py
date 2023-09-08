from bvs.abstract.serializers import AbstractSerializer
from bvs.burncause.models import BurnCause


class BurnCauseSerializer(AbstractSerializer):
    class Meta:
        model = BurnCause
        fields = [
            "id",
            "burn_cause",
            "created",
            "updated",
        ]

