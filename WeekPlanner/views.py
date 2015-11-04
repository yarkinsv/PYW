from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, Context, loader
import datetime
from .models import *
from .choices import *
import pdb


class DayPlan:

    def __init__(self, date):
        self.date = date
        self.day = DayOfWeek.Days[date.weekday()]

        phys = list(PhysicalActivityResult.objects.filter(date=date)[:1])
        if phys:
            self.physical_activity_result = phys[0]
        elif date >= datetime.date.today():
            day_plan = list(DayPlanTemplate.objects.filter(day=DayOfWeek.Days[date.weekday()].value)[:1])
            if day_plan:
                self.physical_activity_result = PhysicalActivityResult()
                self.physical_activity_result.date = date
                self.physical_activity_result.planned_activity = day_plan[0].physical_activity

        edu = list(EducationalActivityResult.objects.filter(date=date)[:1])
        if edu:
            self.educational_activity_result = edu[0]
        elif date >= datetime.date.today():
            day_plan = list(DayPlanTemplate.objects.filter(day=DayOfWeek.Days[date.weekday()].value)[:1])
            if day_plan:
                self.educational_activity_result = EducationalActivityResult()
                self.educational_activity_result.date = date
                self.educational_activity_result.planned_activity = day_plan[0].educational_activity

        task = list(SingleTask.objects.filter(date=date)[:1])
        if task:
            self.single_task = task[0]


class WeekPlanManager:

    def __init__(self):
        self.week_today = datetime.date.today()
        self.week_begin = self.week_today - datetime.timedelta(days=self.week_today.weekday())
        self.week_end = self.week_today + datetime.timedelta(days=6 - self.week_today.weekday())

        self.week_plans = []
        for i in range(7):
            day_plan = DayPlan(date=self.week_begin + datetime.timedelta(days=i))
            self.week_plans.append(day_plan)

        for plan in self.week_plans:
            if plan and plan.date < self.week_today:
                plan.IsPast = True
            elif plan and plan.date == self.week_today:
                plan.IsToday = True
            elif plan:
                plan.IsFuture = True


def index(request):
    manager = WeekPlanManager()
    day_frame_template = loader.get_template('main/day_frame_template.html')
    request_context = RequestContext(request)
    day_frame_templates = [day_frame_template.render(Context({'day_plan': x})) for x in manager.week_plans]
    request_context.push({'manager': manager, 'day_frame_templates': day_frame_templates})
    return render(request, 'main/main.html', request_context)


def educational_activity_result_id(request, activity_id):
    activity = get_object_or_404(EducationalActivityResult, pk=activity_id)
    if request.method == 'POST':
        if not activity.is_future():
            if 'result' in request.POST:
                activity.result = ActivityResult.getresult(request.POST['result'])
            else:
                activity.result = ActivityResult.Unsuccessful
            activity.comment = request.POST['comment']
        if not activity.is_past():
            activity.planned_activity = get_object_or_404(EducationalActivity, pk=int(request.POST['planned_activity']))
            activity.planned_result = request.POST['planned_result']
        activity.save()
        return HttpResponseRedirect("/")
    else:
        activity_types = list(EducationalActivity.objects.all())
        request_context = RequestContext(request)
        request_context.push({'activity': activity, 'activity_types': activity_types})
        template = loader.get_template('main/educational_activity_result_form.html')
        form = template.render(request_context)
        return HttpResponse(form)


def educational_activity_result_create(request, year, month, day):
    activity_date = datetime.date(int(year), int(month), int(day))
    edu = list(EducationalActivityResult.objects.filter(date=activity_date)[:1])
    if edu:
        activity_result = edu[0]
    else:
        activity_result = EducationalActivityResult()
        activity_result.date = activity_date
        activity_result.save()
    return educational_activity_result_id(request, activity_result.id)


def educational_activity_result_create_activity_id(request, year, month, day, activity_id):
    activity_date = datetime.date(int(year), int(month), int(day))
    edu = list(EducationalActivityResult.objects.filter(date=activity_date)[:1])
    if edu:
        activity_result = edu[0]
    else:
        activity_result = EducationalActivityResult()
        activity_result.planned_activity = get_object_or_404(EducationalActivity, pk=int(activity_id))
        activity_result.date = activity_date
        activity_result.save()
    return educational_activity_result_id(request, activity_result.id)


def physical_activity_result_id(request, activity_id):
    activity = get_object_or_404(PhysicalActivityResult, pk=activity_id)
    if request.method == 'POST':
        if request.POST['respond'] == 'confirm':
            if not activity.is_future():
                if 'result' in request.POST:
                    activity.result = ActivityResult.getresult(request.POST['result'])
                else:
                    activity.result = ActivityResult.Unsuccessful
                activity.comment = request.POST['comment']
            if not activity.is_past():
                activity.planned_activity = get_object_or_404(PhysicalActivity, pk=int(request.POST['planned_activity']))
            activity.save()
        elif request.POST['respond'] == 'delete':
            activity.delete()
        return HttpResponseRedirect("/")
    elif request.method == 'GET':
        activity_types = list(PhysicalActivity.objects.all())
        exercises = list(Exercise.objects.all())
        request_context = RequestContext(request)
        request_context.push({'activity': activity, 'activity_types': activity_types, 'exercises': exercises})
        template = loader.get_template('main/physical_activity_result_form.html')
        form = template.render(request_context)
        return HttpResponse(form)


def physical_activity_result_create(request, year, month, day):
    activity_date = datetime.date(int(year), int(month), int(day))
    phys = list(PhysicalActivityResult.objects.filter(date=activity_date)[:1])
    if phys:
        activity_result = phys[0]
    else:
        activity_result = PhysicalActivityResult()
        activity_result.date = activity_date
        activity_result.save()
    return physical_activity_result_id(request, activity_result.id)


def physical_activity_result_create_activity_id(request, year, month, day, activity_id):
    activity_date = datetime.date(int(year), int(month), int(day))
    phys = list(PhysicalActivityResult.objects.filter(date=activity_date)[:1])
    if phys:
        activity_result = phys[0]
    else:
        activity_result = PhysicalActivityResult()
        activity_result.planned_activity = get_object_or_404(PhysicalActivity, pk=int(activity_id))
        activity_result.date = activity_date
        activity_result.save()
    return physical_activity_result_id(request, activity_result.id)


def single_task_id(request, task_id):
    task = get_object_or_404(SingleTask, pk=task_id)
    if request.method == 'POST':
        if request.POST['respond'] == 'confirm':
            if not task.is_future():
                if 'result' in request.POST:
                    task.result = ActivityResult.getresult(request.POST['result'])
                else:
                    task.result = ActivityResult.Unsuccessful
                task.comment = request.POST['comment']
            task.description = request.POST['description']
            task.name = request.POST['name']
            task.save()
        elif request.POST['respond'] == 'delete':
            task.delete()
        return HttpResponseRedirect("/")
    elif request.method == 'GET':
        request_context = RequestContext(request)
        template = loader.get_template('main/single_task_form.html')
        request_context.push({'task': task})
        form = template.render(request_context)
        return HttpResponse(form)


def single_task_create(request, year, month, day):
    task_date = datetime.date(int(year), int(month), int(day))
    task_list = list(SingleTask.objects.filter(date=task_date)[:1])
    if task_list:
        task = task_list[0]
    else:
        task = SingleTask()
        task.date = task_date
        task.save()
    return single_task_id(request, task.id)
