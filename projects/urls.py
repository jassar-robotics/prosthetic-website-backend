from django.urls import include, path
from rest_framework.routers import DefaultRouter

from projects.views.project_views import (ProjectViewSet, ProjectDetailView,) 
from projects.views.statusboard_views import StatusboardViewSet, StatusboardDetailView

router = DefaultRouter()
router.register(r"projects", ProjectViewSet, basename="project")
router.register(r"statusboards", StatusboardViewSet, basename="statusboard")


urlpatterns = [
    path("projects/detail/<slug:project_slug>/", ProjectDetailView.as_view(), name="get-projects"),
    path("", include(router.urls)),

    path("statusboards/detail/<slug:statusboard_slug>/", StatusboardDetailView.as_view(), name="get-statusboards"),
    path("", include(router.urls)),
]
