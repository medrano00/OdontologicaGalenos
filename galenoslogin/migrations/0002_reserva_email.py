# Generated by Django 4.2.10 on 2024-06-09 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galenoslogin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
    ]
