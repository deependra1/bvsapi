from bvs.abstract.serializers import AbstractSerializer
from bvs.hospital.models import Hospital


class HospitalSerializer(AbstractSerializer):
    class Meta:
        model = Hospital
        fields = [
            "id",
            "hospital_name",
            "created",
            "updated",
        ]

