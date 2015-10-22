from djchoices import DjangoChoices, ChoiceItem


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

    @staticmethod
    def getname(choice):
        if choice == "W":
            return "Workout"
        elif choice == "C":
            return "Cardio"
        elif choice == "S":
            return "Sport"
        else:
            return None

