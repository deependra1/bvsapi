from rest_framework import serializers

from bvs.abstract.serializers import AbstractSerializer
from bvs.treatment.models import Treatment
from bvs.patient.models import Patient
from bvs.hospital.models import Hospital
from bvs.hospital.serializers import HospitalSerializer
from datetime import datetime, date


class TreatmentSerializer(AbstractSerializer):
    patient = serializers.SlugRelatedField(
        queryset=Patient.objects.all(), slug_field="public_id"
    )

    hospital = serializers.SlugRelatedField(
        queryset=Hospital.objects.all(), slug_field="public_id"
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
        hospital = Hospital.objects.get_object_by_public_id(rep["hospital"])
        rep["hospital"] = HospitalSerializer(hospital, context=self.context).data

        return rep

    class Meta:
        model = Treatment
        fields = [
            "id",
            "patient",
            "hospital",
            "hospitalized_date",
            "doctor_name",
            "dischared_date",
            "expired_date",
            "mode_of_transport",
            "distance",
            "time",
            "duration_of_stay",
            "no_of_surgery",
            "no_of_skin_graft",
            "no_of_debridement",
            "no_of_amputation",
            "no_of_dressing",
            "no_of_nutritional",
            "medical_support",
            "is_post_treatment",
            "created",
            "updated",
        ]
