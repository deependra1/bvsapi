from django.db.models import Sum
from django.http.response import Http404
from rest_framework.decorators import action
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False)
    def fundings_count(self, request):
        funding_count = Funding.objects.count()
        return Response({'funding_count': funding_count})

    @action(detail=False, methods=['get'])
    def pivoted_funding(self, request):
        pivoted_data = Funding.objects.values('donor').annotate(total_amount=Sum('funding_amount'))

        return Response({'pivoted_data': pivoted_data})
