from decouple import config

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        # ('simple_log', '0001_initial'),
        # ('simple_log', '0002_simplelog_related_logs'),
        # ('simple_log', '0003_auto_20171002_1318'),
        # ('simple_log', '0004_auto_20180614_0727'),
        ('divulgacionAppVRIP', '0011_auto_20191206_2026'),
    ]
    def generate_superuser(apps, schema_editor):
        from django.contrib.auth.models import User

        DEFAULT_SUPERUSER_NAME = config('DEFAULT_SUPERUSER_NAME', default='admin')
        DEFAULT_SUPERUSER_EMAIL = config('DEFAULT_SUPERUSER_EMAIL', default='admin@example.com')
        DEFAULT_SUPERUSER_PASSWORD = config('DEFAULT_SUPERUSER_PASSWORD', default='qwerty123')

        superuser = User.objects.create_superuser(
            username=DEFAULT_SUPERUSER_NAME,
            email=DEFAULT_SUPERUSER_EMAIL,
            password=DEFAULT_SUPERUSER_PASSWORD)
        superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]
