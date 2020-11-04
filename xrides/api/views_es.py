from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from api import documents as booking_documents
from api import serializers as booking_serializers

class BookingViewSet(DocumentViewSet):
    document = booking_documents.BookingDocument
    serializer_class = booking_serializers.BookingDocumentSerializer

    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]

    # Define search fields
    search_fields = (
        'id',
        'user_id',
    )

    # Filter fields
    filter_fields = {
        'id': {
            'field': 'id',
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ],
        },
        'to_city_id': 'to_city_id.raw',
        'from_city_id': 'from_city_id.raw',
        'user_id': {
            'field': 'user_id',
            'lookups': [
                LOOKUP_QUERY_IN,
            ]
        },
    }

    ordering_fields = {
        'id': 'id',
        'to_city_id':'to_city_id'
    }

