from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from bvs.abstract.viewsets import AbstractViewSet
from bvs.hospital.models import Hospital
from bvs.hospital.serializers import HospitalSerializer


class HospitalViewSet(AbstractViewSet):
    http_method_names = ("post", "get", "put", "delete")
    permission_classes = (IsAuthenticated,)
    serializer_class = HospitalSerializer

    def get_queryset(self):
        return Hospital.objects.all().order_by('-created')

    def get_object(self):
        obj = Hospital.objects.get_object_by_public_id(self.kwargs["pk"])

        self.check_object_permissions(self.request, obj)

        return obj

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
