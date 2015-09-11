# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WeekPlanner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayplantemplate',
            name='educational_activity',
            field=models.ForeignKey(to='WeekPlanner.EducationalActivity', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dayplantemplate',
            name='physic_activity',
            field=models.ForeignKey(to='WeekPlanner.PhysicActivity', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dayplantemplate',
            name='single_task',
            field=models.ForeignKey(to='WeekPlanner.SingleTask', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='educationalactivity',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='link',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='physicactivity',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='singletask',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
