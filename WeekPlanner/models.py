from django.db import models
from django.utils import timezone
from datetime import date
from WeekPlanner.choices import *


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class ExerciseResult(models.Model):
    exercise = models.ForeignKey(Exercise)
    working_weight = models.IntegerField()


class WorkoutProgram(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return self.name


class EducationalActivity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class EducationalActivityResult(models.Model):
    date = models.DateField(default=timezone.now())
    planned_activity = models.ForeignKey(EducationalActivity, null=True)
    planned_result = models.TextField(null=True, blank=True, default='')
    result = models.CharField(max_length=1,
                              choices=ActivityResult.choices,
                              validators=[ActivityResult.validator],
                              null=True, blank=True,
                              default=ActivityResult.Unsuccessful)
    comment = models.TextField(null=True, blank=True, default='')

    def week_day_name(self):
        return DayOfWeek.Days[self.date.weekday()].name if self.date else ''

    def is_past(self):
        return self.date < date.today()

    def is_future(self):
        return self.date > date.today()

    def __str__(self):
        return self.planned_activity.name if self.planned_activity else 'a'


class PhysicalActivity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=1,
                            choices=PhysicActivityType.choices,
                            validators=[PhysicActivityType.validator])
    program = models.ForeignKey(WorkoutProgram, null=True, blank=True)

    def type_name(self):
        return PhysicActivityType.getname(self.type)

    def __str__(self):
        return self.name + " (" + self.type_name() + ")"


class PhysicalActivityResult(models.Model):
    date = models.DateField(default=timezone.now())
    planned_activity = models.ForeignKey(PhysicalActivity, null=True)
    result = models.CharField(max_length=1,
                              choices=ActivityResult.choices,
                              validators=[ActivityResult.validator],
                              null=True, blank=True)
    comment = models.TextField(null=True, blank=True, default='')
    exercise_results = models.ManyToManyField(ExerciseResult)

    def week_day_name(self):
        return DayOfWeek.Days[self.date.weekday()].name if self.date else ''

    def is_past(self):
        return self.date < date.today()

    def is_future(self):
        return self.date > date.today()

    def __str__(self):
        return self.planned_activity.name if self.planned_activity else ''


class SingleTask(models.Model):
    date = models.DateField(default=timezone.now())
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    result = models.CharField(max_length=1,
                              choices=ActivityResult.choices,
                              validators=[ActivityResult.validator],
                              null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def week_day_name(self):
        return DayOfWeek.Days[self.date.weekday()].name if self.date else ''

    def is_past(self):
        return self.date < date.today()

    def is_future(self):
        return self.date > date.today()

    def __str__(self):
        return self.planned_activity.name if self.planned_activity else ''


class DayPlanTemplate(models.Model):
    day = models.CharField(max_length=1,
                           choices=DayOfWeek.choices,
                           validators=[DayOfWeek.validator])
    physical_activity = models.ForeignKey(PhysicalActivity, null=True, blank=True)
    educational_activity = models.ForeignKey(EducationalActivity, null=True, blank=True)

    def __str__(self):
        return self.day

