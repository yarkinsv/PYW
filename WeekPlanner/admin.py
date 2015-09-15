from django.contrib import admin

from .models import *

admin.site.register(Exercise)
admin.site.register(WorkoutProgram)
admin.site.register(EducationalActivity)
admin.site.register(PhysicalActivity)
admin.site.register(SingleTask)
admin.site.register(DayPlanTemplate)
admin.site.register(DayPlan)
