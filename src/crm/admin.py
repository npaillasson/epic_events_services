from django.contrib import admin
from .models import Client, Contract, Event

admin.site.register(Client)
admin.site.register(Contract)
#admin.site.register(Event)

# Register your models here.

@admin.register(Event)
class Event(admin.ModelAdmin):
    model = Event

    def get_queryset(self, request):
        user = request.user