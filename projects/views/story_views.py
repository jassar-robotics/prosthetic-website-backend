from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.permissions import AllowAnyAPIView
from projects.models import  Story
from projects.serializer import ( StorySerializer)

class StoryViewSet(ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(modified_at=timezone.now())

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "Story created successfully!", "data": response.data},
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(
            {"message": "Story updated successfully!", "data": response.data},
            status=status.HTTP_200_OK,
        )

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response(
            {"message": "Story deleted successfully!"}, status=status.HTTP_204_NO_CONTENT
        )
