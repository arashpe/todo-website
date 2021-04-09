from django.db import models


class DailyTasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400, blank=True, null=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class RoutineTasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400, blank=True, null=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
