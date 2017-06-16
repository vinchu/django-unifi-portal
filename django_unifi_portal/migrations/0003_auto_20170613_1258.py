# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-13 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_unifi_portal', '0002_auto_20170612_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='unifiuser',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='unifiuser',
            name='guest_mac',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='unifiuser',
            name='last_backend_login',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='unifiuser',
            name='phone',
            field=models.CharField(max_length=255, null=True),
        ),
    ]