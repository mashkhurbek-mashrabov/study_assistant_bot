# Generated by Django 5.0 on 2024-01-07 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_quote_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='was_send',
            field=models.BooleanField(default=False),
        ),
    ]
