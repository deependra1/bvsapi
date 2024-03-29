from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from bvs.abstract.viewsets import AbstractViewSet
from bvs.user.serializers import UserSerializer
from bvs.user.models import User
from bvs.auth.permissions import UserPermission


class UserViewSet(AbstractViewSet):
    http_method_names = ("post", "patch", "get", "delete")
    # permission_classes = (
    #     IsAuthenticated,
    #     UserPermission,
    # )
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)

    # def get_queryset(self):
    #     return User.objects.all()

    def get_object(self):
        obj = User.objects.get_object_by_public_id(self.kwargs["pk"])

        # self.check_object_permissions(self.request, obj)

        return obj

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
