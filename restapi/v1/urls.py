# -*- coding: utf-8 -*-
## Author: Aziz Khan
## License: GPL v3
## Copyright © 2017 Aziz Khan <azez.khan__AT__gmail.com>

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.cache import cache_page

from . import views

#cache timeout in seconds

CACHE_TIMEOUT = 60 * 60  #24 hours
#CACHE_TIMEOUT = 0


urlpatterns = [

	url(r'^$', views.APIRoot.as_view(), name='api-root'),

    url(r'^species/?$', views.SpeciesListViewSet.as_view(), name='species-list'),
    #url(r'^species/(?P<species_name>.+)/$', views.SpeciesDetailsViewSet.as_view(), name='species-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json','jsonp','bed','yaml','api'])