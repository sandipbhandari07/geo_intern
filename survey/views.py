from rest_framework import viewsets
from .models import Survey, SurveyQuestion, SurveyData
from .serializers import SurveySerializer, SurveyQuestionSerializer, SurveyDataSerializer

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class SurveyQuestionViewSet(viewsets.ModelViewSet):
    queryset = SurveyQuestion.objects.all()
    serializer_class = SurveyQuestionSerializer

class SurveyDataViewSet(viewsets.ModelViewSet):
    queryset = SurveyData.objects.all()
    serializer_class = SurveyDataSerializer
