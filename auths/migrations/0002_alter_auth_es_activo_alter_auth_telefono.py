from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth',
            name='es_activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='auth',
            name='telefono',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
