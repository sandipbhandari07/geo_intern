from django.urls import path, include
from rest_framework import routers
from .views import FeatureViewSet

router = routers.DefaultRouter()
router.register(r'', FeatureViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
