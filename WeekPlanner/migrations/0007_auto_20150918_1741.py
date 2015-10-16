# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djchoices.choices


class Migration(migrations.Migration):

    dependencies = [
        ('WeekPlanner', '0006_auto_20150918_1735'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SingleTaskResult',
        ),
        migrations.AddField(
            model_name='singletask',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='singletask',
            name='result',
            field=models.CharField(blank=True, null=True, max_length=1, validators=[djchoices.choices.ChoicesValidator({'U': 'Unsuccessful', 'C': 'Successful'})], choices=[('C', 'Successful'), ('U', 'Unsuccessful')]),
        ),
    ]
