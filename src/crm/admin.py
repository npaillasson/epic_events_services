from django.contrib import admin
from .models import Client, Contract, Events

admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Events)

# Register your models here.
