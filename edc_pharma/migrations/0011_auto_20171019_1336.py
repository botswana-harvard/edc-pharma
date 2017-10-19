# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-19 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edc_pharma', '0010_auto_20171019_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicationdefinition',
            name='formula',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='is_consented',
            field=models.NullBooleanField(default=False),
        ),
    ]