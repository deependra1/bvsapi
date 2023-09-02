from bvs.abstract.serializers import AbstractSerializer
from bvs.family.models import Family


class FamilySerializer(AbstractSerializer):
    class Meta:
        model = Family
        fields = [
            "id",
            "family_type",
            "created",
            "updated",
        ]

