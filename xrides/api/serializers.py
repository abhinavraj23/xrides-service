from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from api.documents import BookingDocument

class BookingDocumentSerializer(DocumentSerializer):
    class Meta:
        document = BookingDocument

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'id',
            'user_id',
            'to_city_id',
            'from_city_id',
        ]