def partial_update(serializer, data, obj):
    for key in data.keys():
            obj.__dict__[key] = serializer.validated_data.get(key)
    obj.save()