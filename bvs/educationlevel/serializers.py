from bvs.abstract.serializers import AbstractSerializer
from bvs.educationlevel.models import EducationLevel


class EducationLevelSerializer(AbstractSerializer):
    class Meta:
        model = EducationLevel
        fields = [
            "id",
            "education_level",
            "created",
            "updated",
        ]

