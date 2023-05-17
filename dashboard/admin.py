from django.contrib import admin
from .models import Task, Note, SharedItem, Draft

admin.site.register(Task)
admin.site.register(Note)
admin.site.register(SharedItem)
admin.site.register(Draft)