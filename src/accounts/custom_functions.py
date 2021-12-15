from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


def is_in_group(user, group):
    return user.groups.filter(name=str(group)).exists()


def username_creation(first_name, last_name):
    username = last_name + first_name[:1]
    if not get_user_model().objects.filter(username=username):
        return username
    i = 1
    while i:
        username_auto_incremented = username + str(i)
        if not get_user_model().objects.filter(username=username_auto_incremented):
            return username_auto_incremented
        i += 1


def assignement_is_superuser(team):
    match team:
        case "1":
            return True
        case _:
            return False


def assignment_of_groups(team, user):
    user.groups.clear()
    print(user.groups.all())
    match team:
        case "1":
            return None
        case "2":
            print(user)
            group = Group.objects.get(name="vente")
            print(group)
            group.user_set.add(user)
            group.save()

        case "3":
            print(user)
            group = Group.objects.get(name="support")
            print('hehehe',group)
            group.user_set.add(user)
            group.save()

