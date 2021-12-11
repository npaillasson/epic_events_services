from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound
from .models import Client, Contract, Event

def partial_update(serializer, data, obj):
    for key in data.keys():
        obj.__dict__[key] = serializer.validated_data.get(key)
    obj.save()


def get_client(id):
    return get_object(id, Client)


def get_contract(id):
    return get_object(id, Contract)


def get_event(id):
    return get_object(id, Event)


def get_object(id, model):
    try:
        queryset = model.objects.get(id=id)
    except ObjectDoesNotExist:
        raise NotFound
    return queryset