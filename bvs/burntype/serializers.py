from bvs.abstract.serializers import AbstractSerializer
from bvs.burntype.models import BurnType


class BurnTypeSerializer(AbstractSerializer):
    class Meta:
        model = BurnType
        fields = [
            "id",
            "burn_type",
            "created",
            "updated",
        ]

