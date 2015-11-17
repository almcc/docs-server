from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = patterns(
    '',

    url(r'^$',
        views.home,
        name='home'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
