from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl import DocType, Index, fields
from api import models as booking_models
from django.conf import settings

ES_INDEX = settings.ES_INDEX

# html_strip = analyzer(
#     'html_strip',
#     tokenizer="standard",
#     filter=["standard", "lowercase", "stop", "snowball"],
#     char_filter=["html_strip"]
# )

@ES_INDEX.doc_type
class BookingDocument(DocType):
    class Meta:
        model = booking_models.Booking

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'uuid',
            'user_id',
            'to_city_id',
            'from_city_id',
        ]
