# Generated by Django 5.0 on 2024-01-01 10:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
                ('telegram_id', models.CharField(max_length=20)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='university.group')),
            ],
            options={
                'ordering': ['-created_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
    ]