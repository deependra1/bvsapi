from django.http.response import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from bvs.abstract.viewsets import AbstractViewSet
from bvs.funding.models import Funding
from bvs.funding.serializers import FundingSerializer


class FundingViewSet(AbstractViewSet):
    http_method_names = ("post", "get", "put", "delete")
    permission_classes = (IsAuthenticated,)
    serializer_class = FundingSerializer

    # def get_queryset(self):
    #     return Funding.objects.all().order_by('-created')

    def get_queryset(self):
        patient_pk = self.kwargs["patient_pk"]
        if patient_pk is None:
            return Http404
        queryset = Funding.objects.filter(patient__public_id=patient_pk)

        return queryset

    def get_object(self):
        obj = Funding.objects.get_object_by_public_id(self.kwargs["pk"])

        self.check_object_permissions(self.request, obj)

        return obj

    # def list(self, request, *args, **kwargs):
    #     patient_pk = self.kwargs["patient_pk"]
    #     donor_pk = self.kwargs["donor_pk"]
    #
    #     queryset = Funding.objects.filter(patient__public_id=patient_pk, donor__public_id=donor_pk)
    #     serializer = FundingSerializer(queryset, many=True)
    #
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
