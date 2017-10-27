# -*- coding: utf-8 -*-
## Author: Aziz Khan
## License: GPL v3
## Copyright © 2017 Aziz Khan <azez.khan__AT__gmail.com>

import os
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.reverse import reverse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.throttling import UserRateThrottle

from rest_framework import renderers

from rest_framework_jsonp.renderers import JSONPRenderer
from rest_framework_yaml.renderers import YAMLRenderer
from rest_framework_yaml.parsers import YAMLParser

from rest_framework.response import Response

from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView, 
    )
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
    BaseFilterBackend,
    DjangoFilterBackend,
    )


class SpeciesListViewSet(ListAPIView):
    """
    REST API endpoint that returns a list of all species supported.
    """
    
    throttle_classes = (UserRateThrottle,)
    filter_backends = [SearchFilter, OrderingFilter, ]
    parser_classes = (YAMLParser,)
    renderer_classes = [ renderers.JSONRenderer, JSONPRenderer, YAMLRenderer, renderers.BrowsableAPIRenderer]

    def get(self, request):
        """
        List all all species supported.
        """

        #####----CODE goes here to call the Perl script to read stdout and put into the species list-----#######

        species = ['A','B','X','Y',Z]

        data_dict = {"species": species}
        
        return Response(data_dict)


class APIRoot(APIView):
    """
    The root of the RSAT RESTful API v1.
    """

    permission_classes = (AllowAny,)

    def get(self, request, format=format):
        return Response({
            'species': reverse('v1:species-list', request=request),
        })


def _get_api_root_url(request):
    return request.build_absolute_uri(location='/')+'api/v1/'

def _get_host_name(request):
    return request.build_absolute_uri(location='/')


    

