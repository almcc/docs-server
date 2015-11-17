from .models import Collection, Product, Release, Artifact
from .serializers import CollectionSerializer, ProductSerializer
from .serializers import ReleaseSerializer, ArtifactSerializer
from rest_framework import generics
from django.http import HttpResponse
import json
from django.shortcuts import render


class CollectionList(generics.ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class CollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_fields = ('name', )


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReleaseList(generics.ListCreateAPIView):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
    filter_fields = ('name', 'product')


class ReleaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer


class ArtifactList(generics.ListCreateAPIView):
    queryset = Artifact.objects.all()
    serializer_class = ArtifactSerializer
    filter_fields = ('name', 'release')


class ArtifactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artifact.objects.all()
    serializer_class = ArtifactSerializer


def path_tree(request):
    paths = []
    for product in Product.objects.all():
        paths.append(product.name)
        for release in product.releases.all():
            paths.append('{}/{}'.format(product.name, release.name))
            for artifact in release.artifacts.all():
                paths.append('{}/{}/{}'.format(product.name,
                                               release.name,
                                               artifact.name))

    return HttpResponse(json.dumps(paths))


def home(request):
    collections = Collection.objects.all()
    uncategorized = Product.objects.filter(collections=None)
    context = {'collections': collections, 'uncategorized': uncategorized}
    return render(request, 'home.html', context)
