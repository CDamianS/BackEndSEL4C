# Generated by Django 4.2.5 on 2023-10-14 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_usuario_respuestasi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='genero',
            field=models.CharField(blank=True, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otro', 'Otro'), ('prefiero_no_decir', 'Prefiero no decirlo')], max_length=50),
        ),
    ]
