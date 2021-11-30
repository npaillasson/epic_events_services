from django.contrib import admin
from .models import Client, Contract, Event
from accounts.custom_functions import is_in_group
from accounts.models import User

#admin.site.register(Client)
#admin.site.register(Contract)
#admin.site.register(Event)

# Register your models here.

class ClientInLine(admin.TabularInline):
    model = Client
    readonly_fields = ("first_name",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event
    def telephone_du_client(self, inst):
        return inst.contract.client.phone_number
    def email_du_client(self, inst):
        return inst.contract.client.email
    def entreprise(self, inst):
        return inst.contract.client.company

    def get_readonly_fields(self, request, obj=None):
        if is_in_group(request.user, "support"):
            return ["support_manager", "telephone_du_client", "entreprise", "email_du_client",]
        return ["telephone_du_client", "entreprise", "email_du_client",]


    list_display = ["id", "event_name", "status", "support_manager","start_date", "end_date", "contract", "telephone_du_client", "entreprise", "email_du_client"]
    #readonly_fields = ["telephone_du_client", "entreprise", "email_du_client",]

    def get_queryset(self, request):
        user = request.user
        if is_in_group(user, 'support'):
            return request.user.support_manager.all()
        return self.model.objects.all()

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    model = Contract
    def telephone_du_client(self, inst):
        return inst.client.phone_number
    def email_du_client(self, inst):
        return inst.client.email
    def entreprise(self, inst):
        return inst.client.company
    def evenement(self, inst):
        return inst.contract
    list_display = ["id", "client", "signature_date", "amount", "telephone_du_client", "entreprise", "email_du_client",
                    "evenement"]
    readonly_fields = ["telephone_du_client", "entreprise", "email_du_client",
                    "evenement"]

    def get_queryset(self, request):
        user = request.user
        if is_in_group(user, 'support'):
            events_concerned = request.user.support_manager.all()
            contract_list = []
            for event in events_concerned:
                contract_list.append(event.contract.id)
            return Contract.objects.filter(id__in=contract_list)
        return self.model.objects.all()

@admin.register(Client)
class ContractAdmin(admin.ModelAdmin):
    model = Client

    def get_queryset(self, request):
        user = request.user
        if is_in_group(user, 'support'):
            events_concerned = request.user.support_manager.all()
            contract_list = []
            client_list = []
            for event in events_concerned:
                contract_list.append(event.contract.id)
            contract_concerned = Contract.objects.filter(id__in=contract_list)
            for contract in contract_concerned:
                client_list.append(contract.client.id)
            return Client.objects.filter(id__in=client_list)
        return self.model.objects.all()

