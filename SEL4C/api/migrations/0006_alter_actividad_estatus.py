# Generated by Django 4.2.5 on 2023-09-30 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_actividad_estatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='estatus',
            field=models.CharField(choices=[('completado', 'Completado'), ('no_completado', 'No completado')], default=2, max_length=25),
        ),
    ]
