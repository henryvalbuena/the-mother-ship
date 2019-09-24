from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Meta, Project

from projects.serializers import ProjectSerializer


PROJECT_URL = reverse('projects:project-list')


def sample_project(user, **kwargs):
    """Create and return a sample recipe"""
    defaults = {
        'title': 'Sample project',
        'name': 'Simply a test'
    }
    defaults.update(kwargs)

    return Project.objects.create(user=user, **defaults)


class PublicProjectAPITests(TestCase):
    """Test unauthenticated projects API access"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test that authentication is required"""
        res = self.client.get(PROJECT_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateProjectAPITests(TestCase):
    """Test authorized projects API access"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@corp.com',
            'secret'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_projects(self):
        """Test retrieving a list of projects"""
        sample_project(user=self.user)
        sample_project(user=self.user)

        res = self.client.get(PROJECT_URL)

        projects = Project.objects.all().order_by('-id')
        serializer = ProjectSerializer(projects, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
