# Generated by Django 4.2.5 on 2023-10-05 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_cuestionariofinal_pregunta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='estatus',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]