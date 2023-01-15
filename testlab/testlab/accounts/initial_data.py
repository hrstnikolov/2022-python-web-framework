from django.contrib.auth.management import create_permissions
from django.contrib.auth.models import Group, Permission


def populate_groups(apps, schema_editor):
    # Create user groups
    roles_and_accessible_models = {
        "Design Engineer": ['customer', 'specification', 'validationtest', ],
        "Lab Engineer": ['', ],
    }

    for name in roles_and_accessible_models.keys():
        Group.objects.create(name=name)

    # Permissions have to be created before applying them
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, verbosity=0)
        app_config.models_module = None

    # Assign model-level permissions to maintainers
    all_perms = Permission.objects.all()
    unique_groups = list(Group.objects.values_list('name').distinct())
    for group in unique_groups:
        accessible_models = roles_and_accessible_models[group]
        permissions = [p for p in all_perms if p.content_type.model in accessible_models]
        Group.objects.get(name=group).permissions.add(*permissions)


# # TODO: Data migration
# from django.db import migrations
# from testlab.accounts.initial_data import populate_groups
#
#
# class Migration(migrations.Migration):
#     dependencies = [
#         ("accounts", "0001_initial"),
#     ]
#
#     operations = [accounts.RunPython(populate_groups)]