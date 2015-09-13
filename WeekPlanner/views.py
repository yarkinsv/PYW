from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
import datetime

from .models import DayPlanTemplate, DayPlan

class WeekPlanManager:

    week_today = datetime.datetime.today()
    week_begin = week_today - datetime.timedelta(days=week_today.weekday())
    week_end = week_today + datetime.timedelta(days=6 - week_today.weekday())

    def __init__(self, **kwargs):                
        return super().__init__(**kwargs)


def index(request):
    plan = get_object_or_404(DayPlanTemplate, pk=1)        
    manager = WeekPlanManager()
    return render(request, 'main/main.html', {'plan': plan, 'manager': manager})