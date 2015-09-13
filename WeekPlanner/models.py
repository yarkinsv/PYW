from django.db import models
from djchoices import DjangoChoices, ChoiceItem


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
    class ActivityResult(DjangoChoices):
        Successful = ChoiceItem("C")
        Unsuccessful = ChoiceItem("U")

    planned = models.TextField(null=True, blank=True)
    result = models.CharField(max_length=1, 
                            choices=ActivityResult.choices, 
                            validators=[ActivityResult.validator],
                            null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

class PhysicalActivity(models.Model):
    class PhysicActivityType(DjangoChoices):
        WorkOut = ChoiceItem("W")
        Cardio = ChoiceItem("C")
        Sport = ChoiceItem("S") 

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=1, 
                            choices=PhysicActivityType.choices, 
                            validators=[PhysicActivityType.validator])
    program = models.ForeignKey(WorkoutProgram, null=True, blank=True)

    def __str__(self):
        return self.name

class PhysicalActivityResult(models.Model):
    class ActivityResult(DjangoChoices):
        Successful = ChoiceItem("C")
        Unsuccessful = ChoiceItem("U")

    planned_activity = models.ForeignKey(PhysicalActivity)
    result = models.CharField(max_length=1, 
                            choices=ActivityResult.choices, 
                            validators=[ActivityResult.validator],
                            null=True, blank=True)
    exercise_results = models.ManyToManyField(ExerciseResult)

class SingleTask(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class SingleTaskResult(models.Model):
    class ActivityResult(DjangoChoices):
        Successful = ChoiceItem("C")
        Unsuccessful = ChoiceItem("U")

    result = models.CharField(max_length=1, 
                            choices=ActivityResult.choices, 
                            validators=[ActivityResult.validator],
                            null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

class DayPlanTemplate(models.Model): 
    class DayOfWeek(DjangoChoices):
        Monday = ChoiceItem("Mn")
        Tuesday = ChoiceItem("Tu")
        Wednesday = ChoiceItem("We")
        Thursday = ChoiceItem("Th")
        Friday = ChoiceItem("Fr")
        Saturday = ChoiceItem("Sa")
        Sunday = ChoiceItem("Su")
     
    day = models.CharField(max_length=2,
                           choices=DayOfWeek.choices,
                           validators=[DayOfWeek.validator])
    physical_activity = models.ForeignKey(PhysicalActivity, null=True, blank=True)
    educational_activity = models.ForeignKey(EducationalActivity, null=True, blank=True)    

    def __str__(self):
        return self.day

class DayPlan():
    class DayOfWeek(DjangoChoices):
        Monday = ChoiceItem("Mn")
        Tuesday = ChoiceItem("Tu")
        Wednesday = ChoiceItem("We")
        Thursday = ChoiceItem("Th")
        Friday = ChoiceItem("Fr")
        Saturday = ChoiceItem("Sa")
        Sunday = ChoiceItem("Su")

    day = models.CharField(max_length=2,
                           choices=DayOfWeek.choices,
                           validators=[DayOfWeek.validator])
    date = models.DateField()
    physical_activity = models.ForeignKey(PhysicalActivity, null=True, blank=True)
    physical_activity_result = models.ForeignKey(PhysicalActivityResult, null=True, blank=True)
    educational_activity = models.ForeignKey(EducationalActivity, null=True, blank=True)
    educational_activity_result = models.ForeignKey(EducationalActivityResult, null=True, blank=True)
    single_task = models.ForeignKey(SingleTask, null=True, blank=True)

    def __str__(self):
        return self.day