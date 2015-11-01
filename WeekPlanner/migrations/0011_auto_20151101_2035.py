# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('WeekPlanner', '0010_auto_20151030_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationalactivityresult',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 11, 1, 17, 35, 33, 665207, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='physicalactivityresult',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 11, 1, 17, 35, 33, 666208, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='singletask',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 11, 1, 17, 35, 33, 667209, tzinfo=utc)),
        ),
    ]
