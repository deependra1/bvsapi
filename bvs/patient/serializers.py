from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from bvs.abstract.serializers import AbstractSerializer
from bvs.patient.models import Patient

from bvs.user.models import User
from bvs.user.serializers import UserSerializer

from bvs.occupation.models import Occupation
from bvs.occupation.serializers import OccupationSerializer

from bvs.ethnic.models import Ethnic
from bvs.ethnic.serializers import EthnicSerializer

from bvs.religion.models import Religion
from bvs.religion.serializers import ReligionSerializer

from bvs.family.models import Family
from bvs.family.serializers import FamilySerializer

from bvs.burncause.models import BurnCause
from bvs.burncause.serializers import BurnCauseSerializer

from bvs.burntype.models import BurnType
from bvs.burntype.serializers import BurnTypeSerializer


# from bvs.user.models import User
# from bvs.user.serializers import UserSerializer


class PatientSerializer(AbstractSerializer):
    creator = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="public_id"
    )

    patient_occupation = serializers.SlugRelatedField(
        queryset=Occupation.objects.all(), slug_field="public_id"
    )

    suppose_occupation = serializers.SlugRelatedField(
        queryset=Occupation.objects.all(), slug_field="public_id"
    )

    parents_occupation = serializers.SlugRelatedField(
        queryset=Occupation.objects.all(), slug_field="public_id"
    )

    ethnic_group = serializers.SlugRelatedField(
        queryset=Ethnic.objects.all(), slug_field="public_id"
    )

    religion = serializers.SlugRelatedField(
        queryset=Religion.objects.all(), slug_field="public_id"
    )

    family_type = serializers.SlugRelatedField(
        queryset=Family.objects.all(), slug_field="public_id"
    )

    burn_cause = serializers.SlugRelatedField(
        queryset=BurnCause.objects.all(), slug_field="public_id"
    )

    burn_type = serializers.SlugRelatedField(
        queryset=BurnType.objects.all(), slug_field="public_id"
    )

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        creator = User.objects.get_object_by_public_id(rep["creator"])

        patient_occupation = Occupation.objects.get_object_by_public_id(rep["patient_occupation"])
        suppose_occupation = Occupation.objects.get_object_by_public_id(rep["suppose_occupation"])
        parents_occupation = Occupation.objects.get_object_by_public_id(rep["parents_occupation"])

        ethnic_group = Ethnic.objects.get_object_by_public_id(rep["ethnic_group"])
        religion = Religion.objects.get_object_by_public_id(rep["religion"])
        family_type = Family.objects.get_object_by_public_id(rep["family_type"])

        burn_cause = BurnCause.objects.get_object_by_public_id(rep["burn_cause"])
        burn_type = BurnType.objects.get_object_by_public_id(rep["burn_type"])

        rep["creator"] = UserSerializer(creator, context=self.context).data

        rep["patient_occupation"] = OccupationSerializer(patient_occupation, context=self.context).data
        rep["suppose_occupation"] = OccupationSerializer(suppose_occupation, context=self.context).data
        rep["parents_occupation"] = OccupationSerializer(parents_occupation, context=self.context).data

        rep["ethnic_group"] = EthnicSerializer(ethnic_group, context=self.context).data
        rep["religion"] = ReligionSerializer(religion, context=self.context).data
        rep["family_type"] = FamilySerializer(family_type, context=self.context).data

        rep["burn_cause"] = BurnCauseSerializer(burn_cause, context=self.context).data
        rep["burn_type"] = BurnTypeSerializer(burn_type, context=self.context).data

        return rep

    class Meta:
        model = Patient
        # List of all the fields that can be included in a request or a response
        fields = [
            "id",
            "creator",
            "registration_date",
            "fiscal_year",
            "registration_location",
            "registration_number",
            "fname",
            "lname",
            "mname",
            "country",
            "provence",
            "district",
            "local",
            "ward",
            "tole",
            "foreign_address",
            "country2",
            "provence2",
            "district2",
            "local2",
            "ward2",
            "tole2",
            "foreign_address2",
            "date_of_birth",
            "age_at_incident",
            "month_at_incident",
            "gender",
            "citizenship_no",
            "patient_contact",
            "parents_contact",
            "optional_contact",
            "patient_education",
            "patient_language",
            "patient_occupation",
            "suppose_occupation",
            "parents_occupation",
            "ethnic_group",
            "religion",
            "family_type",
            "material_status",
            "number_of_child",
            "number_of_siblings",
            "economic_status",
            "family_support",
            "pregnant_women",
            "lactating_mother",
            "with_disabilities",
            "mental_illness",
            "epilepsy",
            "hiv_positive",
            "echo_other",
            "date_of_incident",
            "area_of_burn",
            "percentage_of_burn",
            "degree_of_burn",
            "burn_cause",
            "burn_type",
            "place_of_incident",
            "description_of_incident",
            "person_at_hospital",
            "relation_to_parent",
            "person_contact",
            "created",
            "updated",
        ]
        # read_only_fields = ["edited"]
