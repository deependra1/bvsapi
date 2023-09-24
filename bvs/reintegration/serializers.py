from rest_framework import serializers

from bvs.abstract.serializers import AbstractSerializer
from bvs.question.models import Question
from bvs.question.serializers import QuestionSerializer
from bvs.reintegration.models import Reintegration
from bvs.patient.models import Patient


class ReintegrationSerializer(AbstractSerializer):
    question = serializers.SlugRelatedField(
        queryset=Question.objects.all(), slug_field="public_id"
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
        question = Question.objects.get_object_by_public_id(rep["question"])
        rep["question"] = QuestionSerializer(question, context=self.context).data

        return rep

    class Meta:
        model = Reintegration
        # List of all the fields that can be included in a request or a response
        fields = [
            "id",
            "patient",
            "question",
            "answer",
            "created",
            "updated",
        ]
