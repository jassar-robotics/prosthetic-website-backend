from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.permissions import AllowAnyAPIView
from projects.models import Project
from projects.serializer import (ProjectSerializer)


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(modified_at=timezone.now())

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "Project created successfully!", "data": response.data},
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(
            {"message": "Project updated successfully!", "data": response.data},
            status=status.HTTP_200_OK,
        )

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response(
            {"message": "Project deleted successfully!"}, status=status.HTTP_204_NO_CONTENT
        )

class ProjectDetailView(AllowAnyAPIView):
    def get(self, _, project_slug):
        try:
            project = Project.shown.get(slug=project_slug)
        except Project.DoesNotExist:
            return Response(
                {"error": "Project not found."}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectListView(AllowAnyAPIView):
    def get(self, _):
        try:
            project = Project.shown.all()
        except Project.DoesNotExist:
            return Response(
                {"error": "Project not found."}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)
