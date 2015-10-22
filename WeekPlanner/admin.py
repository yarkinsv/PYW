from django.contrib import admin

from .models import *

admin.site.register(DayPlanTemplate)
admin.site.register(PhysicalActivity)
admin.site.register(Exercise)
admin.site.register(WorkoutProgram)