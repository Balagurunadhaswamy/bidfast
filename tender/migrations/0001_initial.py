# Generated by Django 4.2.6 on 2023-10-18 18:09

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.PositiveBigIntegerField()),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+919999999999'. Up to 15 digits allowed.", regex='^(\\+91[\\-\\s]?)?[0]?(91)?[789]\\d{9}$')])),
                ('address', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TenderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2023, 10, 18))),
                ('company_name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=20)),
                ('prop_summary', models.TextField()),
                ('proj_planning', models.TextField()),
                ('financing', models.CharField(choices=[('bs', 'Bootstarp'), ('cf', 'Crowd Funding'), ('ai', 'Angel Investors'), ('vc', 'Venture Capitalist')], max_length=25)),
                ('sender', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tender.employee')),
            ],
        ),
    ]