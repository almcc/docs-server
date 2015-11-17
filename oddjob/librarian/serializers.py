from django.forms import widgets
from rest_framework import serializers
from .models import Collection, Product, Release, Artifact


class CollectionSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Collection


class ProductSerializer(serializers.ModelSerializer):
    collections = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    releases = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Product


class ReleaseSerializer(serializers.ModelSerializer):
    artifacts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Release


class ArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
