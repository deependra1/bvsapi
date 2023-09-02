from bvs.abstract.serializers import AbstractSerializer
from bvs.religion.models import Religion


class ReligionSerializer(AbstractSerializer):
    class Meta:
        model = Religion
        fields = [
            "id",
            "religion",
            "created",
            "updated",
        ]

