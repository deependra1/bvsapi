from rest_framework import serializers

from bvs.abstract.serializers import AbstractSerializer
from bvs.donor.models import Donor
from bvs.donor.serializers import DonorSerializer
from bvs.funding.models import Funding
from bvs.patient.models import Patient


class FundingSerializer(AbstractSerializer):
    donor = serializers.SlugRelatedField(
        queryset=Donor.objects.all(), slug_field="public_id"
    )
    patient = serializers.SlugRelatedField(
        queryset=Patient.objects.all(), slug_field="public_id"
    )

    def validate_patient(self, value):
        if self.instance:
            return self.instance.patient
        return value

    # def validate_donor(self, value):
    #     if self.instance:
    #         return self.instance.donor
    #     return value

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)

        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        donor = Donor.objects.get_object_by_public_id(rep["donor"])
        rep["donor"] = DonorSerializer(donor, context=self.context).data

        return rep

    class Meta:
        model = Funding
        # List of all the fields that can be included in a request or a response
        fields = [
            "id",
            "patient",
            "donor",
            "funding_amount",
            "created",
            "updated",
        ]
