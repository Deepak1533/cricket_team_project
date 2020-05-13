# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-06 18:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cricket_series', '0003_auto_20200505_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='player_history',
            name='team',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='cricket_series.Team'),
            preserve_default=False,
        ),
    ]