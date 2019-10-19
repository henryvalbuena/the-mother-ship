from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Meta, Project

from projects import serializers


# Create your views here.
class MetaViewSet(viewsets.ModelViewSet):
    """Manage meta in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Meta.objects.all()
    serializer_class = serializers.MetaSerializer

    def get_queryset(self):
        """Return meta for the current authenticated user only"""
        assigned_only = bool(
            int(self.request.query_params.get('assigned_only', 0))
        )
        queryset = self.queryset
        if assigned_only:
            queryset = queryset.filter(recipe__isnull=False)

        return queryset.filter(
            user=self.request.user
        ).order_by('-name').distinct()

    def perform_create(self, serializer):
        """Create a new meta"""
        serializer.save(user=self.request.user)


class ProjectViewSet(viewsets.ModelViewSet):
    """Manage projects in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializer

    def get_queryset(self):
        """Return projects fro the current authenticated user only"""
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Create a new recipe"""
        serializer.save(user=self.request.user)
