from rest_framework import viewsets
from .models import SharedItem, Task, Note, Draft
from .serializers import SharedItemSerializer, TaskSerializer, NoteSerializer, DraftSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class DraftViewSet(viewsets.ModelViewSet):
    queryset = Draft.objects.all()
    serializer_class = DraftSerializer

class SharedItemViewSet(viewsets.ModelViewSet):
    queryset = SharedItem.objects.all()
    serializer_class = SharedItemSerializer
