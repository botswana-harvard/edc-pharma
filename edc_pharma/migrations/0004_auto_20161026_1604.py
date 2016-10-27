# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-26 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edc_pharma', '0003_auto_20161026_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dispense',
            name='syrup_dose',
        ),
        migrations.RemoveField(
            model_name='dispense',
            name='total_dosage_volume',
        ),
        migrations.AddField(
            model_name='dispense',
            name='dose',
            field=models.CharField(blank=True, help_text='Only required if dispense type SYRUP or SOLUTION is chosen', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dispense',
            name='total_volume',
            field=models.CharField(blank=True, help_text='Only required if dispense type SYRUP or IV and or IM is chosen', max_length=10, null=True),
        ),
    ]