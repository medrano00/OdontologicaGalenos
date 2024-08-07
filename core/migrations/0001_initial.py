# Generated by Django 5.0.7 on 2024-07-26 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=20)),
                ('sucursal', models.CharField(max_length=100)),
                ('prevision', models.CharField(max_length=100)),
                ('especialidad', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
