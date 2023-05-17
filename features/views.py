from rest_framework import viewsets
from .models import Feature
from .serializers import FeatureSerializer

class FeatureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
