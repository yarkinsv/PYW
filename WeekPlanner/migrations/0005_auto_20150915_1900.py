# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djchoices.choices


class Migration(migrations.Migration):

    dependencies = [
        ('WeekPlanner', '0004_dayplan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayplan',
            name='day',
            field=models.CharField(max_length=2, validators=[djchoices.choices.ChoicesValidator({'6': 'Sunday', '2': 'Wednesday', '5': 'Saturday', '3': 'Thursday', '4': 'Friday', '1': 'Tuesday', '0': 'Monday'})], choices=[('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')]),
        ),
        migrations.AlterField(
            model_name='dayplantemplate',
            name='day',
            field=models.CharField(max_length=2, validators=[djchoices.choices.ChoicesValidator({'6': 'Sunday', '2': 'Wednesday', '5': 'Saturday', '3': 'Thursday', '4': 'Friday', '1': 'Tuesday', '0': 'Monday'})], choices=[('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')]),
        ),
    ]
