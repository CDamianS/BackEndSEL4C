# Generated by Django 4.2.5 on 2023-10-01 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_actividad_nombre_alter_usuario_edad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividad',
            name='entregable',
        ),
    ]
