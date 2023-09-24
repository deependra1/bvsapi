from bvs.abstract.serializers import AbstractSerializer
from bvs.question.models import Question


class QuestionSerializer(AbstractSerializer):
    class Meta:
        model = Question
        fields = [
            "id",
            "questionnaire",
            "created",
            "updated",
        ]

