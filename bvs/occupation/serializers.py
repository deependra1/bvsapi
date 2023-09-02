from bvs.abstract.serializers import AbstractSerializer
from bvs.occupation.models import Occupation


class OccupationSerializer(AbstractSerializer):
    class Meta:
        model = Occupation
        fields = [
            "id",
            "occupation_name",
            "created",
            "updated",
        ]

