from rest_framework import serializers
from accounts.models import User
from accounts.serializers import ChoiceField
from .models import Client, Contract, Event


class ClientListSerializer(serializers.ModelSerializer):

    client_manager_username = serializers.SerializerMethodField()
    company = serializers.CharField(allow_blank=True, required=True)
    additional_information = serializers.CharField(allow_blank=True, required=True)
    is_client = serializers.CharField(required=True)

    def get_client_manager_username(self, obj):
        return str(obj.client_manager)

    class Meta:
        model = Client
        fields = [
        "id",
        "first_name",
        "last_name",
        "company",
        "email",
        "phone_number",
        "additional_information",
        "client_manager",
        "client_manager_username",
        "is_client",
        ]

class ContractSerializer(serializers.ModelSerializer):
    pass

class EventSerializer(serializers.ModelSerializer):
    pass