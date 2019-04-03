from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters

from rest_framework import permissions, status
from rest_framework.exceptions import APIException
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_auth.app_settings import PasswordChangeSerializer

from django_start.apps.account.serializers import RegisterSerializer, UserProfileSerializer
from django_start.utils.shortcuts import get_message_from_exception

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(
        'password', 'old_password', 'new_password1', 'new_password2'
    )
)


class Register(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                token = serializer.create(serializer.validated_data)
                return Response({'token': token}, status=status.HTTP_201_CREATED)
            except Exception as e:
                raise APIException(e)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UserProfileSerializer(instance=request.user, data=request.data)
        if serializer.is_valid():
            try:
                token = serializer.update(request.user.profile, serializer.validated_data)
                return Response({'token': token}, status=status.HTTP_201_CREATED)
            except Exception as e:
                raise APIException(e)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user = request.user
        profile = user.profile
        data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'phone': profile.phone,
            'email': user.email,
            'address': profile.address,
            'username': user.username,
        }
        return Response(data, status=status.HTTP_200_OK)

class PasswordChangeView(GenericAPIView):
    """
    Calls Django Auth SetPasswordForm save method.

    Accepts the following POST parameters: new_password1, new_password2
    Returns the success/fail message.
    """
    serializer_class = PasswordChangeSerializer
    permission_classes = (IsAuthenticated,)

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(PasswordChangeView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(request.user)
            token = jwt_encode_handler(payload)
        except Exception as e:
            raise APIException(get_message_from_exception(e))

        return Response({'token': token}, status=status.HTTP_200_OK)