# Generated by Django 4.2.8 on 2023-12-17 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moto', '0003_alter_trabajador_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariologin',
            name='rol',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Trabajadores'), (2, 'Clientes')], default=1),
        ),
    ]
