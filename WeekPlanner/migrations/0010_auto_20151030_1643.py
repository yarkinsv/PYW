# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('WeekPlanner', '0009_auto_20151016_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationalactivityresult',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 10, 30, 13, 43, 50, 630587, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='physicalactivityresult',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 10, 30, 13, 43, 50, 631587, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='physicalactivityresult',
            name='planned_activity',
            field=models.ForeignKey(null=True, to='WeekPlanner.PhysicalActivity'),
        ),
        migrations.AlterField(
            model_name='singletask',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 10, 30, 13, 43, 50, 633588, tzinfo=utc)),
        ),
    ]
