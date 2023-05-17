from rest_framework import serializers
from .models import SharedItem, Task, Note, Draft
from survey.models import Survey

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class DraftSerializer(serializers.ModelSerializer):
    task = TaskSerializer()
    note = NoteSerializer()
    survey = serializers.PrimaryKeyRelatedField(queryset=Survey.objects.all())

    class Meta:
        model = Draft
        fields = '__all__'

class SharedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedItem
        fields = '__all__'
