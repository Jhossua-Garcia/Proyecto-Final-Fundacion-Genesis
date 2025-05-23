
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0002_alter_auth_es_activo_alter_auth_telefono'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auth',
            old_name='es_activo',
            new_name='is_activo',
        ),
        migrations.RenameField(
            model_name='auth',
            old_name='es_admin',
            new_name='is_admin',
        ),
        migrations.RenameField(
            model_name='auth',
            old_name='es_staff',
            new_name='is_staff',
        ),
        migrations.RenameField(
            model_name='auth',
            old_name='es_superadmin',
            new_name='is_superadmin',
        ),
    ]
