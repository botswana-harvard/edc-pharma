# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-19 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edc_pharma', '0009_auto_20171018_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='arm',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='is_consented',
            field=models.NullBooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='prescription',
            name='medication_description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='subject_identifier',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Body Weight in Kg'),
        ),
    ]