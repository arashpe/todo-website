from django import forms
from .models import DailyTasks, RoutineTasks


class DailTasksForm(forms.ModelForm):
    class Meta:
        model = DailyTasks
        fields = '__all__'


class RoutineTasksForm(forms.ModelForm):
    class Meta:
        model = RoutineTasks
        fields = '__all__'
