# Generated by Django 3.2 on 2023-01-09 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_is_generated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='is_generated',
            name='is_generated',
        ),
    ]
