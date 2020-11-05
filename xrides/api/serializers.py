from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from api.documents import BookingDocument

class BookingDocumentSerializer(DocumentSerializer):
    class Meta:
        document = BookingDocument

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'id',
            'user_id',
            'vehicle_model_id',
            'package_id',
            'travel_id',
            'from_area_id',
            'to_area_id',
            'from_city_id',
            'to_city_id',
            'from_date',
            'to_date',
            'online_booking',
            'mobile_booking',
            'booking_created',
            'from_lat',
            'from_long',
            'to_lat',
            'to_long',
            'car_cancellation',
        ]