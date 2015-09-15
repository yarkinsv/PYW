from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import Context, loader
import datetime
from .models import DayPlanTemplate, DayPlan, DayOfWeek


class WeekPlanManager:
    week_today = datetime.date.today()
    week_begin = week_today - datetime.timedelta(days=week_today.weekday())
    week_end = week_today + datetime.timedelta(days=6 - week_today.weekday())

    week_plans = []
    for i in range(7):
        day_plan = list(DayPlan.objects.filter(date=week_begin + datetime.timedelta(days=i))[:1])
        if day_plan:
            day_plan = day_plan[0]
        else:
            day_plan = list(DayPlanTemplate.objects.filter(day=str(i)))
            if day_plan:
                day_plan = day_plan[0]
            else:
                day_plan = DayPlan()
                day_plan.date = week_begin + datetime.timedelta(days=i)
                day_plan.day = DayOfWeek.Days[i]

        week_plans.append(day_plan)

    for plan in week_plans:
        if plan and plan.date < week_today:
            plan.IsPast = True
        elif plan and plan.date == week_today:
            plan.IsToday = True
        elif plan:
            plan.IsFuture = True


def index(request):
    manager = WeekPlanManager()
    day_frame_template = loader.get_template('main/day_frame_template.html')
    day_frame_templates = [day_frame_template.render(Context({'day_plan': x})) for x in manager.week_plans]
    return render(request, 'main/main.html', {'manager': manager, 'day_frame_templates': day_frame_templates})


def educational_activity_result(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
