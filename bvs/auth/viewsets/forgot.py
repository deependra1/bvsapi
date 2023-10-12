from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from bvs.user.models import User


class ForgotPasswordViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'])
    def forgot_password(self, request):
        email = request.data.get('email')

        if email:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

            token = default_token_generator.make_token(user)
            uid = user.public_id

            reset_url = f'http://localhost:3000/reset-password/{uid}/{token}/'

            subject = 'Password Reset'
            message = f'Click the following link to reset your password: {reset_url}'
            from_email = 'admin@bvsnepal.org'
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list)

            return Response({'detail': 'Password reset email sent'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Email field is required'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def password_reset_confirm(self, request):
        uid = request.data.get('uid')
        token = request.data.get('token')
        new_password = request.data.get('new_password')

        if not uid or not token or not new_password:
            return Response({'detail': 'UID, token, and new_password fields are required'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            # uid = urlsafe_base64_decode(uid)
            user = User.objects.get(public_id=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.set_password(new_password)
            user.save()
            return Response({'detail': 'Password reset successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid UID or token'}, status=status.HTTP_400_BAD_REQUEST)
