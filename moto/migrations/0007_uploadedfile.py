# Generated by Django 4.2.10 on 2024-02-09 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moto', '0006_trabajadorlogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]