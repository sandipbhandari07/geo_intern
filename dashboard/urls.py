from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SharedItemViewSet, TaskViewSet, NoteViewSet, DraftViewSet

router = DefaultRouter()
router.register(r'shared-items', SharedItemViewSet, basename='shared-item')
router.register(r'tasks', TaskViewSet)
router.register(r'notes', NoteViewSet)
router.register(r'drafts', DraftViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
