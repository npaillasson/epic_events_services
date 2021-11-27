from django.contrib import admin
from .models import Client, Contract, Event
from accounts.custom_functions import is_in_group
from accounts.models import User

admin.site.register(Client)
admin.site.register(Contract)
#admin.site.register(Event)

# Register your models here.

@admin.register(Event)
class Event(admin.ModelAdmin):
    model = Event

    def get_queryset(self, request):
        user = request.user
        if is_in_group(user, 'support'):
            print(self.model.objects.filter(support_manager=user))
            return self.model.objects.filter(support_manager=user)
        print(self.model.objects.all())
        return self.model.objects.all()
