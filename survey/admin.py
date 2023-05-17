from django.contrib import admin
from .models import Survey, SurveyData, SurveyQuestion

admin.site.register(Survey)
admin.site.register(SurveyQuestion)
admin.site.register(SurveyData)