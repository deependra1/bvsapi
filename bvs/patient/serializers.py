from collections import OrderedDict

from django.db.models import Sum
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from bvs.abstract.serializers import AbstractSerializer
from bvs.donor.models import Donor
from bvs.donor.serializers import DonorSerializer
from bvs.funding.models import Funding
from bvs.funding.serializers import FundingSerializer
from bvs.patient.models import Patient
from bvs.physiotherapy.models import Physiotherapy
from bvs.physiotherapy.serializers import PhysiotherapySerializer
from bvs.pshychosocial.models import Psychosocial
from bvs.pshychosocial.serializers import PsychosocialSerializer
from bvs.reintegration.models import Reintegration
from bvs.reintegration.serializers import ReintegrationSerializer

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

from bvs.treatment.models import Treatment
from bvs.treatment.serializers import TreatmentSerializer


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

        # Fetch and serialize related data for Treatment
        treatments = Treatment.objects.filter(patient=instance)
        treatment_data = TreatmentSerializer(treatments, many=True, context=self.context).data
        # Fetch and serialize related data for Funding
        fundings = Funding.objects.filter(patient=instance)
        funding_data = FundingSerializer(fundings, many=True, context=self.context).data

        # Fetch and serialize related data for Physiotherapy
        physiotherapies = Physiotherapy.objects.filter(patient=instance)
        physiotherapy_data = PhysiotherapySerializer(physiotherapies, many=True, context=self.context).data

        # Fetch and serialize related data for Psychosocial
        psychosocials = Psychosocial.objects.filter(patient=instance)
        psychosocial_data = PsychosocialSerializer(psychosocials, many=True, context=self.context).data

        # Fetch and serialize related data for reintegrations
        reintegrations = Reintegration.objects.filter(patient=instance)
        reintegration_data = ReintegrationSerializer(reintegrations, many=True, context=self.context).data

        # Fetch the counts of related Treatment and Funding objects
        treatment_count = Treatment.objects.filter(patient=instance).count()
        funding_count = Funding.objects.filter(patient=instance).count()
        physiotherapie_count = Physiotherapy.objects.filter(patient=instance).count()
        psychosocials_count = Psychosocial.objects.filter(patient=instance).count()

        # Fetch the sum of funding_amount from related Funding objects
        funding_sum = Funding.objects.filter(patient=instance).aggregate(total_funding=Sum('funding_amount'))[
            'total_funding']

        surgery_sum = Treatment.objects.filter(patient=instance).aggregate(total_surgery=Sum('no_of_surgery'))[
            'total_surgery']

        skin_graft_sum = Treatment.objects.filter(patient=instance).aggregate(total_skin_graft=Sum('no_of_skin_graft'))[
            'total_skin_graft']
        debridement_sum = Treatment.objects.filter(patient=instance).aggregate(total_debridement=Sum('no_of_debridement'))[
            'total_debridement']
        amputation_sum = Treatment.objects.filter(patient=instance).aggregate(total_amputation=Sum('no_of_amputation'))[
            'total_amputation']
        dressing_sum = Treatment.objects.filter(patient=instance).aggregate(total_dressing=Sum('no_of_dressing'))[
            'total_dressing']
        nutritional_sum = Treatment.objects.filter(patient=instance).aggregate(total_nutritional=Sum('no_of_nutritional'))[
            'total_nutritional']
        medical_support_sum = Treatment.objects.filter(patient=instance).aggregate(total_medical_support=Sum('medical_support'))[
            'total_medical_support']

        rep["creator"] = UserSerializer(creator, context=self.context).data
        rep["patient_occupation"] = OccupationSerializer(patient_occupation, context=self.context).data
        rep["suppose_occupation"] = OccupationSerializer(suppose_occupation, context=self.context).data
        rep["parents_occupation"] = OccupationSerializer(parents_occupation, context=self.context).data

        rep["ethnic_group"] = EthnicSerializer(ethnic_group, context=self.context).data
        rep["religion"] = ReligionSerializer(religion, context=self.context).data
        rep["family_type"] = FamilySerializer(family_type, context=self.context).data

        rep["burn_cause"] = BurnCauseSerializer(burn_cause, context=self.context).data
        rep["burn_type"] = BurnTypeSerializer(burn_type, context=self.context).data

        # Add the related data to the representation
        rep['treatment'] = treatment_data
        rep['funding'] = funding_data
        rep['physiotherapy'] = physiotherapy_data
        rep['psychosocial'] = psychosocial_data
        # rep['reintegration'] = reintegration_data

        # Add the counts to the representation
        rep['treatment_count'] = treatment_count
        rep['funding_count'] = funding_count
        rep['physiotherapie_count'] = physiotherapie_count
        rep['psychosocials_count'] = psychosocials_count

        # Add the funding sum to the representation
        rep['total_funding'] = funding_sum or 0
        rep['total_surgery'] = surgery_sum or 0
        rep['total_skin_graft'] = skin_graft_sum or 0
        rep['total_debridement'] = debridement_sum or 0
        rep['total_amputation'] = amputation_sum or 0
        rep['total_dressing'] = dressing_sum or 0
        rep['total_nutritional'] = nutritional_sum or 0
        rep['total_medical_support'] = medical_support_sum or 0

        # Pivot funding_data by doner_name
        funding_data_pivoted = {}

        for funding_entry in funding_data:
            donor_name = funding_entry.get('donor', {}).get('donor_name', 'null')
            funding_amount = float(funding_entry.get('funding_amount', 0))  # Convert to float if it's a string
            if donor_name not in funding_data_pivoted:
                funding_data_pivoted[donor_name] = 0
            funding_data_pivoted[donor_name] += funding_amount

        rep['funding_piv'] = funding_data_pivoted

        # Pivot question with answer
        pivoted_data = OrderedDict()
        for reintegration in reintegration_data:
            question = reintegration['question']['questionnaire']
            answer = reintegration['answer']
            pivoted_data[question] = answer

        rep['reintegration'] = pivoted_data

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
            "day_at_incident",
            "age_group",
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
