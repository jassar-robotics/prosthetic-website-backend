from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.permissions import AllowAnyAPIView
from projects.models import  Statusboard
from projects.serializer import ( StatusboardSerializer)

class StatusboardViewSet(ModelViewSet):
    queryset = Statusboard.objects.all()
    serializer_class = StatusboardSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(modified_at=timezone.now())

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "Statusboard created successfully!", "data": response.data},
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(
            {"message": "Statusboard updated successfully!", "data": response.data},
            status=status.HTTP_200_OK,
        )

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response(
            {"message": "Statusboard deleted successfully!"}, status=status.HTTP_204_NO_CONTENT
        )

class StatusboardDetailView(AllowAnyAPIView):
    def get(self, _, statusboard_slug):
        try:
            statusboard = Statusboard.shown.get(slug=statusboard_slug)
        except Statusboard.DoesNotExist:
            return Response(
                {"error": "Statusboard not found."}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = StatusboardSerializer(statusboard)
        return Response(serializer.data, status=status.HTTP_200_OK)

