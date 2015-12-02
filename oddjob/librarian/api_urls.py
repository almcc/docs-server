from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = [

    url(r'^collections$',
        views.CollectionList.as_view(),
        name='collections-list'),

    url(r'^collections/(?P<pk>[0-9]+)$',
        views.CollectionDetail.as_view(),
        name='collections-detail'),

    url(r'^products$',
        views.ProductList.as_view(),
        name='products-list'),

    url(r'^products/(?P<pk>[0-9]+)$',
        views.ProductDetail.as_view(),
        name='products-detail'),

    url(r'^releases$',
        views.ReleaseList.as_view(),
        name='releases-list'),

    url(r'^releases/(?P<pk>[0-9]+)$',
        views.ReleaseDetail.as_view(),
        name='releases-detail'),

    url(r'^artifacts$',
        views.ArtifactList.as_view(),
        name='artifacts-list'),

    url(r'^artifacts/(?P<pk>[0-9]+)$',
        views.ArtifactDetail.as_view(),
        name='artifacts-detail'),

    url(r'^path-tree$',
        views.path_tree,
        name='path-tree'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
