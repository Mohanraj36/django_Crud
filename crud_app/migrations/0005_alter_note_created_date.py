# Generated by Django 4.0.5 on 2022-10-04 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0004_alter_note_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(blank=True, default='Asia/Kolkata', null=True),
        ),
    ]
