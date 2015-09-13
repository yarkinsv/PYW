from djchoices import DjangoChoices, ChoiceItem

class DayOfWeek(DjangoChoices):
    Monday = ChoiceItem("Mn")
    Tuesday = ChoiceItem("Tu")
    Wednesday = ChoiceItem("We")
    Thursday = ChoiceItem("Th")
    Friday = ChoiceItem("Fr")
    Saturday = ChoiceItem("Sa")
    Sunday = ChoiceItem("Su")

class PhysicActivityType(DjangoChoices):
    WorkOut = ChoiceItem("W")
    Cardio = ChoiceItem("C")
    Sport = ChoiceItem("S")    

class ActivityResult(DjangoChoices):
    Successful = ChoiceItem("C")
    Unsuccessful = ChoiceItem("U")