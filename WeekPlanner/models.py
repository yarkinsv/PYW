from django.db import models
from djchoices import DjangoChoices, ChoiceItem
from django.utils import timezone
from datetime import date


class DayOfWeek(DjangoChoices):
    Monday = ChoiceItem("0")
    Tuesday = ChoiceItem("1")
    Wednesday = ChoiceItem("2")
    Thursday = ChoiceItem("3")
    Friday = ChoiceItem("4")
    Saturday = ChoiceItem("5")
    Sunday = ChoiceItem("6")

    Monday.name = "Monday"
    Tuesday.name = "Tuesday"
    Wednesday.name = "Wednesday"
    Thursday.name = "Thursday"
    Friday.name = "Friday"
    Saturday.name = "Saturday"
    Sunday.name = "Sunday"

    Days = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]


class ActivityResult(DjangoChoices):
    Successful = ChoiceItem("C")
    Unsuccessful = ChoiceItem("U")

    @staticmethod
    def getresult(option):
        if option == 'on':
            return ActivityResult.Successful
        else:
            return ActivityResult.Unsuccessful


class PhysicActivityType(DjangoChoices):
    WorkOut = ChoiceItem("W")
    Cardio = ChoiceItem("C")
    Sport = ChoiceItem("S")


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class ExerciseResult(models.Model):
    exercise = models.ForeignKey(Exercise)
    weight = models.IntegerField()
    reps = models.IntegerField()
    sets = models.IntegerField()


class WorkoutProgram(models.Model):
    name = models.CharField(max_length=100)
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

    def __str__(self):
        return self.name


class PhysicalActivityResult(models.Model):
    date = models.DateField(default=timezone.now())
    planned_activity = models.ForeignKey(PhysicalActivity)
    planned_result = models.TextField(null=True, blank=True, default='')
    result = models.CharField(max_length=1,
                              choices=ActivityResult.choices,
                              validators=[ActivityResult.validator],
                              null=True, blank=True)
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


class DayPlanTemplate(models.Model):
    day = models.CharField(max_length=1,
                           choices=DayOfWeek.choices,
                           validators=[DayOfWeek.validator])
    physical_activity = models.ForeignKey(PhysicalActivity, null=True, blank=True)
    educational_activity = models.ForeignKey(EducationalActivity, null=True, blank=True)

    def __str__(self):
        return self.day
