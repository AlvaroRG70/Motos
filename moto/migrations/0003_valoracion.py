# Generated by Django 4.2.10 on 2024-02-25 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moto', '0002_alter_moto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Valoracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntuacion', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('comentario', models.TextField()),
                ('concesionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='valoraciones', to='moto.concesionario')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='valoraciones', to='moto.usuario')),
            ],
        ),
    ]
