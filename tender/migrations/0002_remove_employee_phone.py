# Generated by Django 4.2.6 on 2023-10-18 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='phone',
        ),
    ]
