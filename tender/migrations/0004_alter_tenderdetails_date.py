# Generated by Django 4.2.6 on 2023-10-18 19:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0003_tenderdetails_financing_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenderdetails',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
