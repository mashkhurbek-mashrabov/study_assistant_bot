# Generated by Django 5.0 on 2024-01-01 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
