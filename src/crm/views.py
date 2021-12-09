from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Event, Client, Contract
from .serializers import ClientListSerializer
from .api_utilities import partial_update

class DisplayClient(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated]
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


    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        filter_backends = self.filter_queryset(queryset)
        serializer = ClientListSerializer(filter_backends, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        queryset = Client.objects.get(id=self.kwargs["pk"])
        serializer = ClientListSerializer(queryset)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        user = Client.objects.get(id=self.kwargs["pk"])
        self.perform_destroy(user)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        self.object = Client.objects.get(id=self.kwargs["pk"])
        serializer = ClientListSerializer(self.object, data=request.data, partial=True)

        if serializer.is_valid():
            partial_update(serializer, request.data, self.object)
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
