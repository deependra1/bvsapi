from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from bvs.abstract.serializers import AbstractSerializer
# from bvs.user.models import User
# from bvs.user.serializers import UserSerializer
from bvs.treatment.models import Treatment
from bvs.patient.models import Patient


class TreatmentSerializer(AbstractSerializer):
    # author = serializers.SlugRelatedField(
    #     queryset=User.objects.all(), slug_field="public_id"
    # )
    patient = serializers.SlugRelatedField(
        queryset=Patient.objects.all(), slug_field="public_id"
    )

    # def validate_author(self, value):
    #     if self.context["request"].user != value:
    #         raise ValidationError("You can't create a post for another user.")
    #     return value

    def validate_patient(self, value):
        if self.instance:
            return self.instance.patient
        return value

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)

        return instance

    class Meta:
        model = Treatment
        # List of all the fields that can be included in a request or a response
        fields = [
            "id",
            "patient",
            "hospital",
            "hospitalized_date",
            "doctor_name",
            "dischared_date",
            "expired_date",
            "current_status",
            "created",
            "updated",
        ]

