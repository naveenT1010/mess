# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-12 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0004_remove_profile_rfid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='user',
        ),
        migrations.AddField(
            model_name='activity',
            name='profile',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='rating.Profile'),
            preserve_default=False,
        ),
    ]
