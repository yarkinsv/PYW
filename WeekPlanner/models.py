from django.db import models
from djchoices import DjangoChoices, ChoiceItem

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class ExercisePlan(models.Model):
    exercise = models.ForeignKey(Exercise)
    reps = models.IntegerField()
    sets = models.IntegerField()

    def __str__(self):
        return self.exercise.name + " | " + str(self.reps) + " | " + str(self.sets)

class WorkoutProgram(models.Model):
    name = models.CharField(max_length=100)
    exercises = models.ManyToManyField(ExercisePlan)

    def __str__(self):
        return self.name

class EducationalActivity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class PhysicActivity(models.Model):
    
    class PhysicActivityType(DjangoChoices):
        WorkOut = ChoiceItem("W")
        Cardio = ChoiceItem("C")
        Sport = ChoiceItem("S")
        Rest = ChoiceItem("R")

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=1, 
                            choices=PhysicActivityType.choices, 
                            validators=[PhysicActivityType.validator])
    program = models.ForeignKey(WorkoutProgram)

    def __str__(self):
        return self.name

class SingleTask(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

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
    physic_activity = models.ForeignKey(PhysicActivity, null=True, blank=True)
    educational_activity = models.ForeignKey(EducationalActivity, null=True, blank=True)
    single_task = models.ForeignKey(SingleTask, null=True, blank=True)

    def __str__(self):
        return self.day