from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurveyViewSet, SurveyQuestionViewSet, SurveyDataViewSet

router = DefaultRouter()
router.register(r'surveys', SurveyViewSet, basename='survey')
router.register(r'survey-questions', SurveyQuestionViewSet, basename='survey-question')
router.register(r'survey-data', SurveyDataViewSet, basename='survey-data')

urlpatterns = [
    path('', include(router.urls)),
]
