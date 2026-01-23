from django.urls import include, path
from rest_framework.routers import DefaultRouter

from projects.views.project_views import ProjectDetailView, ProjectListView

router = DefaultRouter()
# router.register(r"projects", ProjectViewSet, basename="project")

urlpatterns = [
    path("project/detail/<slug:project_slug>/", ProjectDetailView.as_view(), name="get-project-detail"),
    path("project/list/", ProjectListView.as_view(), name="get-project-list"),
    # path("", include(router.urls)),
]
