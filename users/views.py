from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserRegisterSerializer


class UserRegistrationView(APIView):

    permission_classes = [AllowAny]

    def post(self, *args, **kwargs):
        serializer = UserRegisterSerializer(data=self.request.data)

        serializer.is_valid(raise_exception=True)

        User.objects.create_user(**serializer.validated_data).save()

        return Response(status=201)