# Generated by Django 4.2.10 on 2024-03-03 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moto', '0003_valoracion'),
    ]

    operations = [
        migrations.AddField(
            model_name='moto',
            name='caballos',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='moto',
            name='consumo',
            field=models.FloatField(null=True),
        ),
    ]
