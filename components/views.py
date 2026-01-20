from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.permissions import AllowAnyAPIView
from components.models import  Component
from components.serializer import ( ComponentSerializer)

class ComponentViewSet(ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(modified_at=timezone.now())

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "Component created successfully!", "data": response.data},
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(
            {"message": "Component updated successfully!", "data": response.data},
            status=status.HTTP_200_OK,
        )

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response(
            {"message": "Component deleted successfully!"}, status=status.HTTP_204_NO_CONTENT
        )

class ComponentDetailView(AllowAnyAPIView):
    def get(self, _, component_slug):
        try:
            component = Component.shown.get(slug=component_slug)
        except Component.DoesNotExist:
            return Response(
                {"error": "Component not found."}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = ComponentSerializer(component)
        return Response(serializer.data, status=status.HTTP_200_OK)

