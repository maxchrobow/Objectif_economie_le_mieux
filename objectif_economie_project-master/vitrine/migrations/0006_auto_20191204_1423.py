# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-12-04 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0005_auto_20191204_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bdd_assistance_technique',
            name='equipement',
            field=models.CharField(choices=[('Pompe_a_chaleur', 'Pompe à chaleur'), ('Isolation', 'Isolation'), ('Domotique', 'Domotique'), ('Chaudiere', 'Chaudiere'), ('Ballon_thermodynamique', 'Ballon thermodynamique')], max_length=50, null=True),
        ),
    ]
