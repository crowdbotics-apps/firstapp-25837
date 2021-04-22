from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    TaskerLocationViewSet,
    MapLocationViewSet,
    CustomerLocationViewSet,
    TaskLocationViewSet,
)

router = DefaultRouter()
router.register("customerlocation", CustomerLocationViewSet)
router.register("taskerlocation", TaskerLocationViewSet)
router.register("maplocation", MapLocationViewSet)
router.register("tasklocation", TaskLocationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
