# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djchoices.choices


class Migration(migrations.Migration):

    dependencies = [
        ('WeekPlanner', '0002_auto_20150908_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalActivityResult',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('planned', models.TextField(blank=True, null=True)),
                ('result', models.CharField(null=True, max_length=1, blank=True, validators=[djchoices.choices.ChoicesValidator({'C': 'Successful', 'U': 'Unsuccessful'})], choices=[('C', 'Successful'), ('U', 'Unsuccessful')])),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseResult',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('weight', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('sets', models.IntegerField()),
                ('exercise', models.ForeignKey(to='WeekPlanner.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalActivity',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(max_length=1, validators=[djchoices.choices.ChoicesValidator({'C': 'Cardio', 'W': 'WorkOut', 'S': 'Sport'})], choices=[('W', 'WorkOut'), ('C', 'Cardio'), ('S', 'Sport')])),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalActivityResult',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('result', models.CharField(null=True, max_length=1, blank=True, validators=[djchoices.choices.ChoicesValidator({'C': 'Successful', 'U': 'Unsuccessful'})], choices=[('C', 'Successful'), ('U', 'Unsuccessful')])),
                ('exercise_results', models.ManyToManyField(to='WeekPlanner.ExerciseResult')),
                ('planned_activity', models.ForeignKey(to='WeekPlanner.PhysicalActivity')),
            ],
        ),
        migrations.CreateModel(
            name='SingleTaskResult',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('result', models.CharField(null=True, max_length=1, blank=True, validators=[djchoices.choices.ChoicesValidator({'C': 'Successful', 'U': 'Unsuccessful'})], choices=[('C', 'Successful'), ('U', 'Unsuccessful')])),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='exerciseplan',
            name='exercise',
        ),
        migrations.RemoveField(
            model_name='physicactivity',
            name='program',
        ),
        migrations.RemoveField(
            model_name='dayplantemplate',
            name='physic_activity',
        ),
        migrations.RemoveField(
            model_name='dayplantemplate',
            name='single_task',
        ),
        migrations.AlterField(
            model_name='workoutprogram',
            name='exercises',
            field=models.ManyToManyField(to='WeekPlanner.Exercise'),
        ),
        migrations.DeleteModel(
            name='ExercisePlan',
        ),
        migrations.DeleteModel(
            name='PhysicActivity',
        ),
        migrations.AddField(
            model_name='physicalactivity',
            name='program',
            field=models.ForeignKey(blank=True, null=True, to='WeekPlanner.WorkoutProgram'),
        ),
        migrations.AddField(
            model_name='dayplantemplate',
            name='physical_activity',
            field=models.ForeignKey(blank=True, null=True, to='WeekPlanner.PhysicalActivity'),
        ),
    ]
