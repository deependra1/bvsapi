from django.db.models import Count, Q
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.decorators import action
from django.core.cache import cache

from rest_framework.filters import SearchFilter
from rest_framework import filters
from bvs.abstract.viewsets import AbstractViewSet
from bvs.patient.models import Patient
from bvs.patient.serializers import PatientSerializer


class PatientViewSet(AbstractViewSet):
    http_method_names = ("post", "get", "put", "delete")
    permission_classes = (IsAuthenticated,)
    serializer_class = PatientSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = [
        'registration_date',
        'fiscal_year',
        'registration_location',
        'registration_number',
        'fname',
        'lname',
        'mname',
    ]

    # filterset_fields = ["author__public_id"]

    def get_queryset(self):
        user_location = self.request.user.location

        queryset = Patient.objects.all().order_by('-created')

        if user_location:
            queryset = queryset.filter(Q(registration_location=user_location))

        return queryset

    def get_object(self):
        obj = Patient.objects.get_object_by_public_id(self.kwargs["pk"])

        self.check_object_permissions(self.request, obj)

        return obj

    def list(self, request, *args, **kwargs):
        patient_objects = cache.get("patient_objects")
        if patient_objects is None:
            patient_objects = self.filter_queryset(self.get_queryset())
            cache.set("post_objects", patient_objects)

        serializer = self.get_serializer(patient_objects, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['GET'])
    def get_latest(self, request):
        latest = self.get_queryset()[:10]
        serializer = self.get_serializer(latest, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def patients_count(self, request):
        patient_count = Patient.objects.count()
        return Response({'patient_count': patient_count})

    @action(detail=False)
    def group_by_age(self, request):
        age_groups = (
            Patient.objects.values('age_at_incident')
            .annotate(patient_count=Count('age_at_incident'))
            .order_by('age_at_incident')
        )

        # Convert the queryset into a list for easier serialization
        age_groups_list = list(age_groups)

        return Response(age_groups_list)

    @action(detail=False)
    def group_by_gender(self, request):
        gender_counts = (
            Patient.objects.values('gender')
            .annotate(patient_count=Count('gender'))
            .order_by('gender')
        )

        # Convert the queryset into a list for easier serialization
        gender_counts_list = list(gender_counts)

        return Response(gender_counts_list)

    @action(detail=False)
    def group_by_fiscal(self, request):
        fiscal_year_counts = (
            Patient.objects.values('fiscal_year')
            .annotate(patient_count=Count('fiscal_year'))
            .order_by('fiscal_year')
        )

        # Convert the queryset into a list for easier serialization
        fiscal_year_counts_list = list(fiscal_year_counts)

        return Response(fiscal_year_counts_list)

    @action(detail=False, methods=['GET'])
    def post_treatment_patients(self, request):
        post_treatment_patients = self.get_queryset().filter(treatment__is_post_treatment=True)
        serializer = self.get_serializer(post_treatment_patients, many=True)
        return Response(serializer.data)
