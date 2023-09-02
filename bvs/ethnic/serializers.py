from bvs.abstract.serializers import AbstractSerializer
from bvs.ethnic.models import Ethnic


class EthnicSerializer(AbstractSerializer):
    class Meta:
        model = Ethnic
        fields = [
            "id",
            "ethnic_group",
            "created",
            "updated",
        ]

