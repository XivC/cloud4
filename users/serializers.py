from rest_framework import serializers

from users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        ]