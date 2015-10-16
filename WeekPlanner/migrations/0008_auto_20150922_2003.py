# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import djchoices.choices


class Migration(migrations.Migration):

    dependencies = [
        ('WeekPlanner', '0007_auto_20150918_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dayplan',
            name='educational_activity',
        ),
        migrations.RemoveField(
            model_name='dayplan',
            name='educational_activity_result',
        ),
        migrations.RemoveField(
            model_name='dayplan',
            name='physical_activity',
        ),
        migrations.RemoveField(
            model_name='dayplan',
            name='physical_activity_result',
        ),
        migrations.RemoveField(
            model_name='dayplan',
            name='single_task',
        ),
        migrations.AddField(
            model_name='educationalactivityresult',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 9, 22, 17, 3, 18, 267468, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='physicalactivityresult',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 9, 22, 17, 3, 18, 268468, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='singletask',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 9, 22, 17, 3, 18, 269468, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='dayplantemplate',
            name='day',
            field=models.CharField(choices=[('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')], validators=[djchoices.choices.ChoicesValidator({'1': 'Tuesday', '6': 'Sunday', '2': 'Wednesday', '0': 'Monday', '3': 'Thursday', '4': 'Friday', '5': 'Saturday'})], max_length=1),
        ),
        migrations.DeleteModel(
            name='DayPlan',
        ),
    ]
