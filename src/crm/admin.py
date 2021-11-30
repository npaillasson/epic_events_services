from django.contrib import admin
from .models import Client, Contract, Event
from accounts.custom_functions import is_in_group
from accounts.models import User

#admin.site.register(Client)
#admin.site.register(Contract)
#admin.site.register(Event)

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event

    def get_queryset(self, request):
        user = request.user
        if is_in_group(user, 'support'):
            return request.user.support_manager.all()
        return self.model.objects.all()

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    model = Contract

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