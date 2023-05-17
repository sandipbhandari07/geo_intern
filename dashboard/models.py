from django.db import models
from django.contrib.auth.models import User
from survey.models import Survey

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    additional_note = models.TextField(blank=True)
    geo_data = models.TextField()
    has_route = models.BooleanField(default=False)
    route = models.TextField()
    status = models.CharField(max_length=255, default='todo')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    additional_note = models.TextField(blank=True)
    geo_data = models.TextField()
    status = models.CharField(max_length=255, default='todo')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Draft(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    note = models.OneToOneField(Note, on_delete=models.CASCADE)
    survey = models.OneToOneField(Survey, on_delete=models.CASCADE)
    drafted = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class SharedItem(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    note = models.OneToOneField(Note, on_delete=models.CASCADE)
    survey = models.OneToOneField(Survey, on_delete=models.CASCADE)
    shared_by_user = models.ForeignKey(User, on_delete=models.CASCADE)
    shared_to_emails = models.TextField()

    def __str__(self):
        return self.title
