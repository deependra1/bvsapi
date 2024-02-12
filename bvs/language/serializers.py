from bvs.abstract.serializers import AbstractSerializer
from bvs.language.models import Language


class LanguageSerializer(AbstractSerializer):
    class Meta:
        model = Language
        fields = [
            "id",
            "language_name",
            "created",
            "updated",
        ]

