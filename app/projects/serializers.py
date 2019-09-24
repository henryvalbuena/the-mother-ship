from rest_framework import serializers

from core.models import Meta, Project


class MetaSerializer(serializers.ModelSerializer):
    """Serializer for meta objects"""

    class Meta:
        model = Meta
        fields = ('id', 'name')
        read_only_fields = ('id',)


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for project objects"""
    meta = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Meta.objects.all()
    )

    class Meta:
        model = Project
        fields = (
            'id',
            'title',
            'name',
            'meta',
            'desc',
            'detail',
            'img_url',
            'github'
        )
        read_only_fields = ('id',)
