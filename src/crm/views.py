from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from .models import Event, Client, Contract
from .serializers import ClientListSerializer, ContractSerializer, EventSerializer
from .api_utilities import partial_update, get_client, get_contract, get_event
from .permissions import CanManageClient, CanManageContract, CanManageEvent

class DisplayClient(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated, CanManageClient]
    serializer_class = ClientListSerializer
    filterset_fields = [
            "first_name",
            "last_name",
            "company",
            "email",
            "phone_number",
            "additional_information",
            "client_manager",
            "is_client",
            ]

    def perform_create(self, serializer):

        Client.objects.create(
            first_name=serializer.validated_data["first_name"],
            last_name=serializer.validated_data["last_name"],
            company=serializer.validated_data["company"],
            email=serializer.validated_data["email"],
            phone_number=serializer.validated_data["phone_number"],
            additional_information=serializer.validated_data["additional_information"],
            client_manager=serializer.validated_data["client_manager"],
            is_client=serializer.validated_data["is_client"],
        )
        return Response(serializer.data)


    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        filter_backends = self.filter_queryset(queryset)
        serializer = ClientListSerializer(filter_backends, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        queryset = get_client(id=self.kwargs["pk"])
        serializer = ClientListSerializer(queryset)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        client = get_client(id=self.kwargs["pk"])
        self.perform_destroy(client)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        self.object = get_client(id=self.kwargs["pk"])
        serializer = ClientListSerializer(self.object, data=request.data, partial=True)

        if serializer.is_valid():
            partial_update(serializer, request.data, self.object)
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DisplayContract(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    permission_classes = [IsAuthenticated, CanManageContract]
    serializer_class = ContractSerializer
    filterset_fields = [
            "client",
            "signature_date",
            "amount",
            "additional_information",
            "is_signed",
            ]

    def perform_create(self, serializer):

        Contract.objects.create(
            client=serializer.validated_data["client"],
            amount = serializer.validated_data["amount"],
            additional_information = serializer.validated_data["additional_information"],
            is_signed = serializer.validated_data["is_signed"]
        )
        return Response(serializer.data)


    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        filter_backends = self.filter_queryset(queryset)
        serializer = ContractSerializer(filter_backends, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        queryset = get_contract(id=self.kwargs["pk"])
        serializer = ContractSerializer(queryset)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        contract = get_contract(id=self.kwargs["pk"])
        self.perform_destroy(contract)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        self.object = get_contract(id=self.kwargs["pk"])
        serializer = ContractSerializer(self.object, data=request.data, partial=True)

        if serializer.is_valid():
            partial_update(serializer, request.data, self.object)
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DisplayEvent(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    filterset_fields = [
            "id",
            "contract",
            "support_manager",
            "event_name",
            "start_date",
            "end_date",
            "status",
            "time_created",
            "time_changed"
            ]

    def perform_create(self, serializer):

        Event.objects.create(
            contract=serializer.validated_data["contract"],
            support_manager=serializer.validated_data["support_manager"],
            event_name=serializer.validated_data["event_name"],
            start_date=serializer.validated_data["start_date"],
            end_date=serializer.validated_data["end_date"],
            additional_information=serializer.validated_data["additional_information"],
            status=serializer.validated_data["status"],
        )
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        filter_backends = self.filter_queryset(queryset)
        serializer = EventSerializer(filter_backends, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        queryset = get_event(id=self.kwargs["pk"])
        serializer = EventSerializer(queryset)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        contract = get_event(id=self.kwargs["pk"])
        self.perform_destroy(contract)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        self.object = get_event(id=self.kwargs["pk"])
        serializer = EventSerializer(self.object, data=request.data, partial=True)

        if serializer.is_valid():
            partial_update(serializer, request.data, self.object)
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
