from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl import Document, Index, fields
from api import models as booking_models
from django.conf import settings

ES_INDEX = settings.ES_INDEX

# html_strip = analyzer(
#     'html_strip',
#     tokenizer="standard",
#     filter=["standard", "lowercase", "stop", "snowball"],
#     char_filter=["html_strip"]
# )

@ES_INDEX.document
class BookingDocument(Document):
    class Django:
        model = booking_models.Booking

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
