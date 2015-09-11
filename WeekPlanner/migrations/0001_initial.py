# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djchoices.choices


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DayPlanTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('day', models.CharField(max_length=2, choices=[('Mn', 'Monday'), ('Tu', 'Tuesday'), ('We', 'Wednesday'), ('Th', 'Thursday'), ('Fr', 'Friday'), ('Sa', 'Saturday'), ('Su', 'Sunday')], validators=[djchoices.choices.ChoicesValidator({'Fr': 'Friday', 'Su': 'Sunday', 'We': 'Wednesday', 'Sa': 'Saturday', 'Tu': 'Tuesday', 'Mn': 'Monday', 'Th': 'Thursday'})])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EducationalActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('link', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExercisePlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('reps', models.IntegerField()),
                ('sets', models.IntegerField()),
                ('exercise', models.ForeignKey(to='WeekPlanner.Exercise')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhysicActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=1, choices=[('W', 'WorkOut'), ('C', 'Cardio'), ('S', 'Sport'), ('R', 'Rest')], validators=[djchoices.choices.ChoicesValidator({'R': 'Rest', 'W': 'WorkOut', 'C': 'Cardio', 'S': 'Sport'})])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SingleTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkoutProgram',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('exercises', models.ManyToManyField(to='WeekPlanner.ExercisePlan')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='physicactivity',
            name='program',
            field=models.ForeignKey(to='WeekPlanner.WorkoutProgram'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dayplantemplate',
            name='educational_activity',
            field=models.ForeignKey(to='WeekPlanner.EducationalActivity'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dayplantemplate',
            name='physic_activity',
            field=models.ForeignKey(to='WeekPlanner.PhysicActivity'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dayplantemplate',
            name='single_task',
            field=models.ForeignKey(to='WeekPlanner.SingleTask'),
            preserve_default=True,
        ),
    ]
