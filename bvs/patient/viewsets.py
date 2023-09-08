from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.decorators import action
from django.core.cache import cache

from bvs.abstract.viewsets import AbstractViewSet
from bvs.patient.models import Patient
from bvs.patient.serializers import PatientSerializer


class PatientViewSet(AbstractViewSet):
    http_method_names = ("post", "get", "put", "delete")
    permission_classes = (IsAuthenticated,)
    serializer_class = PatientSerializer

    # filterset_fields = ["author__public_id"]

    def get_queryset(self):
        return Patient.objects.all().order_by('-created')

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
