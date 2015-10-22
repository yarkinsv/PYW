# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import djchoices.choices


class Migration(migrations.Migration):

    dependencies = [
        ('WeekPlanner', '0008_auto_20150922_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exerciseresult',
            old_name='reps',
            new_name='working_weight',
        ),
        migrations.RemoveField(
            model_name='exerciseresult',
            name='sets',
        ),
        migrations.RemoveField(
            model_name='exerciseresult',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='physicalactivityresult',
            name='planned_result',
        ),
        migrations.AddField(
            model_name='physicalactivityresult',
            name='comment',
            field=models.TextField(null=True, default='', blank=True),
        ),
        migrations.AddField(
            model_name='workoutprogram',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='educationalactivityresult',
            name='comment',
            field=models.TextField(null=True, default='', blank=True),
        ),
        migrations.AlterField(
            model_name='educationalactivityresult',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 10, 16, 9, 33, 41, 218607, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='educationalactivityresult',
            name='planned_result',
            field=models.TextField(null=True, default='', blank=True),
        ),
        migrations.AlterField(
            model_name='educationalactivityresult',
            name='result',
            field=models.CharField(choices=[('C', 'Successful'), ('U', 'Unsuccessful')], null=True, blank=True, max_length=1, default='U', validators=[djchoices.choices.ChoicesValidator({'U': 'Unsuccessful', 'C': 'Successful'})]),
        ),
        migrations.AlterField(
            model_name='physicalactivityresult',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 10, 16, 9, 33, 41, 219607, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='singletask',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 10, 16, 9, 33, 41, 221607, tzinfo=utc)),
        ),
    ]
