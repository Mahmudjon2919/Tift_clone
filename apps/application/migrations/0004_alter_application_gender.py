# Generated by Django 5.1 on 2024-09-11 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_application_contract_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='gender',
            field=models.CharField(choices=[('male', 'Erkak'), ('female', 'Ayol')], max_length=6),
        ),
    ]
