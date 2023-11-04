# Generated by Django 3.2.22 on 2023-11-04 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='usuario',
            field=models.ManyToManyField(related_name='reserva_evento', through='moto.ReservaEvento', to='moto.Usuario'),
        ),
    ]