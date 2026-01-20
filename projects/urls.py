from django.urls import include, path
from rest_framework.routers import DefaultRouter

from projects.views import (ProjectViewSet, ProjectDetailView) 

router = DefaultRouter()
router.register(r"projects", ProjectViewSet, basename="project")

urlpatterns = [
    path("projects/detail/<slug:project_slug>/", ProjectDetailView.as_view(), name="get-projects"),
    path("", include(router.urls)),
]
