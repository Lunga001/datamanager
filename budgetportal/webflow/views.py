# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict
from drf_haystack.serializers import HaystackSerializer, HaystackFacetSerializer
from drf_haystack.viewsets import HaystackViewSet
from drf_haystack.mixins import FacetMixin
from budgetportal import models
from ..search_indexes import ProvInfraProjectIndex
from drf_haystack.filters import HaystackFacetFilter, HaystackFilter, HaystackOrderingFilter
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

import json
import decimal
import datetime


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)


def provincial_infrastructure_project_list(request):
    context = {
        "page_title": "Provincial infrastructure project search - vulekamali",
        "page_description": "Find infrastructure projects by provincial departments.",
        "page_data_json": "null",
    }
    return render(
        request, "webflow/infrastructure-search-template.html", context=context
    )


def provincial_infrastructure_project_detail(request, id, slug):
    project = get_object_or_404(models.ProvInfraProject, pk=int(id))
    snapshot = project.project_snapshots.latest()
    page_data = {"project": model_to_dict(snapshot)}
    page_data["project"]["irm_snapshot"] = snapshot.irm_snapshot.__unicode__()
    context = {
        "project": project,
        "page_data_json": json.dumps(
            page_data, cls=JSONEncoder, sort_keys=True, indent=4
        ),
        "page_title": "%s, %s Infrastructure projects - vulekamali"
        % (snapshot.name, snapshot.province),
        "page_description": "Provincial infrastructure project by the %s %s department."
        % (snapshot.province, snapshot.department),
    }
    return render(
        request,
        "webflow/detail_provincial-infrastructure-projects.html",
        context=context,
    )


class ProvInfraProjectSerializer(HaystackSerializer):
    class Meta:
        # The `index_classes` attribute is a list of which search indexes
        # we want to include in the search.
        index_classes = [ProvInfraProjectIndex]

        # The `fields` contains all the fields we want to include.
        # NOTE: Make sure you don't confuse these with model attributes. These
        # fields belong to the search index!
        fields = [
            "name",
            "province",
            "department",
            "status",
            "status_order",
            "primary_funding_source",
            "estimated_completion_date",
            "total_project_cost",
            "url_path",
            "latitude",
            "longitude",
        ]

    def __init__(self, *args, **kwargs):
        # https://www.django-rest-framework.org/api-guide/serializers/#example
        # Instantiate the superclass normally
        super(ProvInfraProjectSerializer, self).__init__(*args, **kwargs)

        fields = self.context["request"].query_params.get("fields")
        if fields:
            fields = fields.split(",")
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class ProvInfraProjectFacetSerializer(HaystackFacetSerializer):

    serialize_objects = True  # Setting this to True will serialize the
    # queryset into an `objects` list. This
    # is useful if you need to display the faceted
    # results. Defaults to False.

    class Meta:
        index_classes = [ProvInfraProjectIndex]
        fields = ["province", "department", "status", "primary_funding_source"]
        field_options = {
            "province": {},
            "department": {},
            "status": {},
            "primary_funding_source": {},
        }


class ProvInfraProjectFacetFilter(HaystackFacetFilter):
    def filter_queryset(self, request, queryset, view, *args, **kwargs):
        queryset = super(ProvInfraProjectFacetFilter, self).filter_queryset(
            request, queryset, view, *args, **kwargs
        )
        text_query = request.query_params.get("q", None)
        if text_query:
            queryset = queryset.filter(text=text_query)
        return queryset


class ProvInfraProjectFilter(HaystackFilter):
    def filter_queryset(self, request, queryset, view, *args, **kwargs):
        queryset = super(ProvInfraProjectFilter, self).filter_queryset(
            request, queryset, view, *args, **kwargs
        )
        text_query = request.query_params.get("q", None)
        if text_query:
            queryset = queryset.filter(text=text_query)
        return queryset


class ProvInfraProjectSearchView(FacetMixin, HaystackViewSet):

    # `index_models` is an optional list of which models you would like to include
    # in the search result. You might have several models indexed, and this provides
    # a way to filter out those of no interest for this particular view.
    # (Translates to `SearchQuerySet().models(*index_models)` behind the scenes.
    # index_models = [Location]

    serializer_class = ProvInfraProjectSerializer
    filter_backends = [ProvInfraProjectFilter, HaystackOrderingFilter]

    facet_serializer_class = ProvInfraProjectFacetSerializer
    facet_filter_backends = [ProvInfraProjectFacetFilter]

    ordering_fields = [
        'name',
        'total_project_cost',
        'status_order',
        'estimated_completion_date',
    ]

    @method_decorator(cache_page(60 * 30))  # minutes
    def get(self, *args, **kwargs):
        super(ProvInfraProjectSearchView, self).get(*args, **kwargs)
