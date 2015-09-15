# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djchoices.choices


class Migration(migrations.Migration):

    dependencies = [
        ('WeekPlanner', '0003_auto_20150913_2053'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayPlan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('day', models.CharField(validators=[djchoices.choices.ChoicesValidator({'Mn': 'Monday', 'We': 'Wednesday', 'Su': 'Sunday', 'Fr': 'Friday', 'Tu': 'Tuesday', 'Sa': 'Saturday', 'Th': 'Thursday'})], max_length=2, choices=[('Mn', 'Monday'), ('Tu', 'Tuesday'), ('We', 'Wednesday'), ('Th', 'Thursday'), ('Fr', 'Friday'), ('Sa', 'Saturday'), ('Su', 'Sunday')])),
                ('date', models.DateField()),
                ('educational_activity', models.ForeignKey(null=True, blank=True, to='WeekPlanner.EducationalActivity')),
                ('educational_activity_result', models.ForeignKey(null=True, blank=True, to='WeekPlanner.EducationalActivityResult')),
                ('physical_activity', models.ForeignKey(null=True, blank=True, to='WeekPlanner.PhysicalActivity')),
                ('physical_activity_result', models.ForeignKey(null=True, blank=True, to='WeekPlanner.PhysicalActivityResult')),
                ('single_task', models.ForeignKey(null=True, blank=True, to='WeekPlanner.SingleTask')),
            ],
        ),
    ]
