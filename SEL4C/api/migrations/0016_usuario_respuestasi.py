# Generated by Django 4.2.5 on 2023-10-14 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_usuario_avance'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='respuestasI',
            field=models.BooleanField(default=False),
        ),
    ]