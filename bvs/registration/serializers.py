from bvs.abstract.serializers import AbstractSerializer
from bvs.registration.models import Registration


class RegistrationSerializer(AbstractSerializer):
    class Meta:
        model = Registration
        fields = [
            "id",
            "registration_date",
            'fiscal_year',
            "registration_location",
            'registration_number',
            "created",
            "updated",
        ]

