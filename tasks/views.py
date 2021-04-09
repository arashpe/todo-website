from django.shortcuts import render, redirect
from .forms import *
from .models import *


def index(request):
    daily_tasks = DailyTasks.objects.all()
    daily_form = DailTasksForm()
    routine_tasks = RoutineTasks.objects.all()
    routine_form = RoutineTasksForm()
    context = {'DailyTasks': daily_tasks, 'RoutineTasks': routine_tasks,
               'DailyForm': daily_form, 'RoutineForm': routine_form}
    if request.method == "POST":
        if request.POST.get('create daily task'):
            form = DailTasksForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("/")
    if request.method == "POST":
        if request.POST.get('create routine task'):
            form = RoutineTasksForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("/")
    return render(request, 'tasks/index.html', context)
