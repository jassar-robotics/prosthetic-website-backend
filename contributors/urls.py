from django.urls import include, path
from rest_framework.routers import DefaultRouter
from contributors.views import (ContributorViewSet, ContributorDetailView) 
router = DefaultRouter()
router.register(r"contributors", ContributorViewSet, basename="contributor")

urlpatterns = [
    # path("contributors/detail/<slug:contributor_slug>/", ContributorDetailView.as_view(), name="get-contributors"),
    # path("", include(router.urls)),
]
