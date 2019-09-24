from django.urls import path, include

from rest_framework.routers import DefaultRouter

from projects import views


router = DefaultRouter()
router.register('meta', views.MetaViewSet)
router.register('projects', views.ProjectViewSet)

app_name = 'projects'

urlpatterns = [
    path('', include(router.urls))
]
