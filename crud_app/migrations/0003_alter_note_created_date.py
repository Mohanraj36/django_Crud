# Generated by Django 4.0.5 on 2022-10-04 16:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0002_note_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
