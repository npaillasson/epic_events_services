from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound
import crm.models as models


def partial_update(serializer, data, obj):
    for key in data.keys():
        obj.__dict__[key] = serializer.validated_data.get(key)
    obj.save()


def get_client(id):
    return get_object(id, models.Client)


def get_contract(id):
    return get_object(id, models.Contract)


def get_event(id):
    return get_object(id, models.Event)


def get_object(id, model):
    try:
        queryset = model.objects.get(id=id)
    except ObjectDoesNotExist:
        raise NotFound
    return queryset