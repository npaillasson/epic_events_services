from django.contrib import admin
from .models import Client, Contract, Event
from accounts.custom_functions import is_in_group
from accounts.models import User

@admin.action(description='Convertir le(s) prospect(s) en client(s)')
def convert_client(Prospect, request, queryset):
    queryset.update(is_client=True)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context['adminform'].form.fields['support_manager'].queryset = User.objects.filter(team="3")
        return super(EventAdmin, self).render_change_form(request, context, add=True, change=True)

    def telephone_du_client(self, inst):
        return inst.contract.client.phone_number
    telephone_du_client.short_description = "téléphone du client"

    def email_du_client(self, inst):
        return inst.contract.client.email
    def entreprise(self, inst):
        return inst.contract.client.company
    def email_du_support_manager(self, inst):
        return inst.support_manager.email

    def get_readonly_fields(self, request, obj=None):
        list_fields = ["telephone_du_client", "entreprise", "email_du_client", "email_du_support_manager"]
        if is_in_group(request.user, "support") or is_in_group(request.user, "vente"):
            list_fields.append("support_manager")
            return list_fields
        return list_fields

    list_display = ["id", "event_name", "status", "support_manager","start_date", "end_date",
                    "contract", "telephone_du_client", "entreprise", "email_du_client"]

    def get_queryset(self, request):
        user = request.user
        if is_in_group(user, 'support'):
            return request.user.support_manager.all()
        return self.model.objects.all()

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    model = Contract

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context['adminform'].form.fields['client'].queryset = Client.objects.filter(is_client=True)
        return super(ContractAdmin, self).render_change_form(request, context, add=True, change=True)

    def telephone_du_client(self, inst):
        return inst.client.phone_number
    telephone_du_client.short_description = "téléphone du client"
    def email_du_client(self, inst):
        return inst.client.email
    def entreprise(self, inst):
        return inst.client.company
    def evenement(self, inst):
        return inst.contract
    evenement.short_description = "évènement"

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
class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ["first_name", "last_name", "company", "phone_number", "email", "client_manager"]

    def commercial_manager_email(self, inst):
        return inst.client_manager.email
    commercial_manager_email.short_description = "email du responsable commercial"

    def get_readonly_fields(self, request, obj=None):
        list_fields = ["commercial_manager_email"]
        if is_in_group(request.user, "support") or is_in_group(request.user, "vente"):
            list_fields.append("client_manager")
            return list_fields
        return list_fields

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context['adminform'].form.fields['client_manager'].queryset = User.objects.filter(team="2")
        return super(ClientAdmin, self).render_change_form(request, context, add=True, change=True)

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ("is_client",)
        form = super(ClientAdmin, self).get_form(request, obj, **kwargs)
        return form

    def save_model(self, request, obj, form, change):
        obj.is_client = True
        super(ClientAdmin, self).save_model(request, obj, form, change)

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
        return self.model.objects.filter(is_client=True)

def create_modeladmin(modeladmin, model, name = None):
    class  Meta:
        proxy = True
        app_label = model._meta.app_label

    attrs = {'__module__': '', 'Meta': Meta}

    newmodel = type(name, (model,), attrs)

    admin.site.register(newmodel, modeladmin)
    return modeladmin

print(ClientAdmin)
class Prospect(ClientAdmin):
    actions = [convert_client]

    def get_form(self, request, obj=None, **kwargs):
        form = super(ClientAdmin, self).get_form(request, obj, **kwargs)
        return form

    def save_model(self, request, obj, form, change):
        super(ClientAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        print("OK")
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
        return self.model.objects.filter(is_client=False)

create_modeladmin(Prospect, model=Client, name="prospect")






