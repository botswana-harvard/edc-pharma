# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edc_pharma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispense',
            name='hostname_created',
            field=models.CharField(default='keletso-mac', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='historicalmedication',
            name='hostname_created',
            field=models.CharField(default='keletso-mac', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='historicalpatient',
            name='hostname_created',
            field=models.CharField(default='keletso-mac', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='medication',
            name='hostname_created',
            field=models.CharField(default='keletso-mac', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='hostname_created',
            field=models.CharField(default='keletso-mac', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='protocol',
            name='hostname_created',
            field=models.CharField(default='keletso-mac', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='site',
            name='hostname_created',
            field=models.CharField(default='keletso-mac', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
    ]
