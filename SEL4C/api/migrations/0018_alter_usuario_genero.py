# Generated by Django 4.2.5 on 2023-10-17 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_usuario_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='genero',
            field=models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro'), ('Prefiero no decir', 'Prefiero no decirlo')], max_length=50),
        ),
    ]
