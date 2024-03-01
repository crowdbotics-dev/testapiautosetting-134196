from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134196ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134196", Testconnectors134196ViewSet, basename="testconnectors134196"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
