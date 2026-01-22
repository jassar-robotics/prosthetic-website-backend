from django.urls import include, path
from rest_framework.routers import DefaultRouter

from projects.views.project_views import ProjectViewSet, ProjectDetailView, ProjectListView
from projects.views.statusboard_views import StatusboardViewSet
from projects.views.story_views import StoryViewSet

router = DefaultRouter()
router.register(r"projects", ProjectViewSet, basename="project")
router.register(r"stories", StatusboardViewSet, basename="story")
router.register(r"usecases", StatusboardViewSet, basename="usecase")
router.register(r"statusboards", StoryViewSet, basename="statusboard")


urlpatterns = [
    path("project/detail/<slug:project_slug>/", ProjectDetailView.as_view(), name="get-project-detail"),
    path("project/list/", ProjectListView.as_view(), name="get-project-list"),


    path("", include(router.urls)),
]
