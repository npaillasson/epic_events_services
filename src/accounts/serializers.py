from rest_framework import serializers
from .models import User, TEAM_CHOICES


class ChoiceField(serializers.ChoiceField):
    def to_representation(self, obj):
        return self._choices[obj]


class AdminUserSerializer(serializers.ModelSerializer):

    team = ChoiceField(TEAM_CHOICES)
    username = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "team",
        ]


class UserSerializer(serializers.ModelSerializer):
    team = ChoiceField(TEAM_CHOICES)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "team",
        ]
