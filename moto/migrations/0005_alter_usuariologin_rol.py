# Generated by Django 4.2.8 on 2023-12-17 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moto', '0004_alter_usuariologin_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariologin',
            name='rol',
            field=models.PositiveSmallIntegerField(choices=[(1, 'trabajador'), (2, 'cliente')], default=1),
        ),
    ]
