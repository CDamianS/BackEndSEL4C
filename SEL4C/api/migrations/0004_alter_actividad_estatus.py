# Generated by Django 4.2.5 on 2023-09-29 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_actividad_estatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='estatus',
            field=models.IntegerField(choices=[(1, 'Completado'), (2, 'No completado')]),
        ),
    ]
