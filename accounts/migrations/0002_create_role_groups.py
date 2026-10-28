from django.db import migrations


ROLE_NAMES = (
    "Customer",
    "Vendor Employee",
    "Platform Admin",
)


def create_role_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")

    for name in ROLE_NAMES:
        Group.objects.get_or_create(name=name)


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_role_groups, migrations.RunPython.noop),
    ]
