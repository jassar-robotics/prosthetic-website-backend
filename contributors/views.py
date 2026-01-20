from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.permissions import AllowAnyAPIView
from contributors.models import  Contributor
from contributors.serializer import ( ContributorSerializer)

class ContributorViewSet(ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(modified_at=timezone.now())

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "Contributor created successfully!", "data": response.data},
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(
            {"message": "Contributor updated successfully!", "data": response.data},
            status=status.HTTP_200_OK,
        )

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response(
            {"message": "Contributor deleted successfully!"}, status=status.HTTP_204_NO_CONTENT
        )

class ContributorDetailView(AllowAnyAPIView):
    def get(self, _, contributor_slug):
        try:
            contributor = Contributor.shown.get(slug=contributor_slug)
        except Contributor.DoesNotExist:
            return Response(
                {"error": "Contributor not found."}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = ContributorSerializer(contributor)
        return Response(serializer.data, status=status.HTTP_200_OK)

