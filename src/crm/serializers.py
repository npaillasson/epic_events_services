from rest_framework import serializers
from accounts.models import User
from .models import Client, Contract, Event, STATUS_CHOICES
from accounts.serializers import ChoiceField


class ClientListSerializer(serializers.ModelSerializer):

    client_manager_username = serializers.SerializerMethodField()
    company = serializers.CharField(allow_blank=True, required=True)
    additional_information = serializers.CharField(allow_blank=True, required=True)
    is_client = serializers.BooleanField(required=True)

    def get_client_manager_username(self, obj):
        try:
            return str(obj.client_manager)
        except AttributeError:
            user = User.objects.get(id=self.initial_data["client_manager"])
            return user.username

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
            "time_created",
            "time_changed",
        ]


class ContractSerializer(serializers.ModelSerializer):
    client_name = serializers.SerializerMethodField()
    client_manager = serializers.SerializerMethodField()
    client_manager_username = serializers.SerializerMethodField()
    event_name = serializers.SerializerMethodField()
    event_id = serializers.SerializerMethodField()
    additional_information = serializers.CharField(allow_blank=True, required=True)
    is_signed = serializers.BooleanField(required=True)

    def get_client_name(self, obj):
        try:
            return str(obj.client)
        except AttributeError:
            client = Client.objects.get(id=obj.client)
            return str(client)

    def get_client_manager(self, obj):
        try:
            return str(obj.client.client_manager.id)
        except AttributeError:
            user = User.objects.get(id=obj.client.client_manager.id)
            return user.id

    def get_client_manager_username(self, obj):
        try:
            return str(obj.client.client_manager)
        except AttributeError:
            user = User.objects.get(id=obj.client.client_manager.id)
            return user.username

    def get_event_name(self, obj):
        try:
            return str(obj.contract)
        except AttributeError:
            return None

    def get_event_id(self, obj):
        try:
            return str(obj.contract.id)
        except AttributeError:
            return None

    class Meta:
        model = Contract

        fields = [
            "id",
            "client",
            "client_name",
            "signature_date",
            "amount",
            "additional_information",
            "is_signed",
            "client_manager",
            "client_manager_username",
            "event_id",
            "event_name",
            "time_created",
            "time_changed",
        ]


class EventSerializer(serializers.ModelSerializer):
    client_id = serializers.SerializerMethodField()
    client_name = serializers.SerializerMethodField()
    client_manager = serializers.SerializerMethodField()
    client_manager_username = serializers.SerializerMethodField()
    additional_information = serializers.CharField(allow_blank=True, required=True)
    status = ChoiceField(STATUS_CHOICES)
    support_manager_username = serializers.SerializerMethodField()

    def get_client_name(self, obj):
        try:
            return str(obj.contract.client)
        except AttributeError:
            contract = Contract.objects.get(id=self.initial_data["contract"])
            client = Client.objects.get(id=contract.client.id)
            return str(client)

    def get_client_id(self, obj):
        try:
            return obj.contract.client.id
        except AttributeError:
            contract = Contract.objects.get(id=self.initial_data["contract"])
            client = Client.objects.get(id=contract.client.id)
            return client.id

    def get_client_manager(self, obj):
        try:
            return obj.contract.client.client_manager.id
        except AttributeError:
            contract = Contract.objects.get(id=self.initial_data["contract"])
            user = User.objects.get(id=contract.client.client_manager.id)
            return user.id

    def get_client_manager_username(self, obj):
        try:
            return str(obj.contract.client.client_manager)
        except AttributeError:
            contract = Contract.objects.get(id=self.initial_data["contract"])
            user = User.objects.get(id=contract.client.client_manager.id)
            return user.username

    def get_support_manager_username(self, obj):
        try:
            return str(obj.support_manager)
        except AttributeError:
            user = User.objects.get(id=self.initial_data["support_manager"])
            return user.username

    class Meta:
        model = Event

        fields = [
            "id",
            "contract",
            "support_manager",
            "support_manager_username",
            "event_name",
            "start_date",
            "end_date",
            "additional_information",
            "status",
            "time_created",
            "time_changed",
            "client_id",
            "client_name",
            "client_manager",
            "client_manager_username",
        ]
