from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from bvs.abstract.serializers import AbstractSerializer
from bvs.followUpSummary.models import FollowUpSummary
from bvs.followUpSummary.serializers import FollowUpSummarySerializer
# from bvs.user.models import User
# from bvs.user.serializers import UserSerializer
from bvs.physiotherapy.models import Physiotherapy
from bvs.patient.models import Patient


class PhysiotherapySerializer(AbstractSerializer):
    patient = serializers.SlugRelatedField(
        queryset=Patient.objects.all(), slug_field="public_id"
    )

    followup_summary = serializers.SlugRelatedField(
        queryset=FollowUpSummary.objects.all(), slug_field="public_id"
    )

    def validate_patient(self, value):
        if self.instance:
            return self.instance.patient
        return value

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)

        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        donor = FollowUpSummary.objects.get_object_by_public_id(rep["followup_summary"])
        rep["followup_summary"] = FollowUpSummarySerializer(donor, context=self.context).data

        return rep

    class Meta:
        model = Physiotherapy
        # List of all the fields that can be included in a request or a response
        fields = [
            "id",
            "patient",
            "initial_status",
            "applied_methods",
            "dischared_status",
            "observation",
            "current_status",
            "mode_of_followup",
            "followed_by",
            "followup_summary",
            "number_of_session",
            "created",
            "updated",
        ]
