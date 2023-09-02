from bvs.abstract.serializers import AbstractSerializer
from bvs.donor.models import Donor


class DonorSerializer(AbstractSerializer):
    class Meta:
        model = Donor
        fields = [
            "id",
            "donor_name",
            "donor_address",
            "created",
            "updated",
        ]

