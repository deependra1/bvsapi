from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.core.cache import cache

from bvs.abstract.viewsets import AbstractViewSet
from bvs.registration.models import Registration
from bvs.registration.serializers import RegistrationSerializer


class RegistrationViewSet(AbstractViewSet):
    http_method_names = ("post", "get", "put", "delete")
    # permission_classes = (IsAuthenticated,)
    serializer_class = RegistrationSerializer

    def get_queryset(self):
        return Registration.objects.all()

    def get_object(self):
        obj = Registration.objects.get_object_by_public_id(self.kwargs["pk"])

        self.check_object_permissions(self.request, obj)

        return obj

    def list(self, request, *args, **kwargs):
        registration_objects = cache.get("registration_objects")
        if registration_objects is None:
            registration_objects = self.filter_queryset(self.get_queryset())
            cache.set("post_objects", registration_objects)

        serializer = self.get_serializer(registration_objects, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
