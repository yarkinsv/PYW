# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WeekPlanner', '0005_auto_20150915_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='educationalactivityresult',
            old_name='planned',
            new_name='planned_result',
        ),
        migrations.AddField(
            model_name='educationalactivityresult',
            name='planned_activity',
            field=models.ForeignKey(to='WeekPlanner.EducationalActivity', null=True),
        ),
        migrations.AddField(
            model_name='physicalactivityresult',
            name='planned_result',
            field=models.TextField(null=True, blank=True),
        ),
    ]
