from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.static import serve
import views
from django.contrib.auth.decorators import login_required


urlpatterns = [

    url(r'^$',
        views.home,
        name='home'),

    url(r'^product/(?P<product>[0-9a-zA-Z_-]+)$',
        views.product,
        name='product'),

    url(r'^product/(?P<product>[0-9a-zA-Z_-]+)/(?P<release>[\.0-9a-zA-Z_-]+)/(?P<artifact>[0-9a-zA-Z_-]+/)$',
        views.artifact,
        name='artifact')
]

urlpatterns = format_suffix_patterns(urlpatterns)
