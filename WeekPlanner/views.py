from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import DayPlanTemplate

def index(request):
    plan = get_object_or_404(DayPlanTemplate, pk=1)        
    return render(request, 'main/main.html', {'plan': plan})