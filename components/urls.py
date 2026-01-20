from django.urls import include, path
from rest_framework.routers import DefaultRouter
from components.views import (ComponentViewSet, ComponentDetailView) 
router = DefaultRouter()
router.register(r"components", ComponentViewSet, basename="component")

urlpatterns = [
    path("components/detail/<slug:component_slug>/", ComponentDetailView.as_view(), name="get-components"),
    path("", include(router.urls)),
]
