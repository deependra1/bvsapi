from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from bvs.auth.serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated


class PasswordChangeViewSet(ViewSet):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["put"]

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.request.user

        # Check if the old password is correct
        if not user.check_password(serializer.validated_data['old_password']):
            return Response({'detail': 'Old password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the new password and retype password match
        new_password = serializer.validated_data['new_password']
        retype_password = serializer.validated_data['retype_password']

        if new_password != retype_password:
            return Response({'detail': 'New password and retype password do not match.'},
                            status=status.HTTP_400_BAD_REQUEST)
        # Change the user's password
        user.set_password(serializer.validated_data['new_password'])
        user.save()

        return Response({'detail': 'Password successfully changed.'}, status=status.HTTP_200_OK)
