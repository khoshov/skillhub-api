from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import ReviewSource


@registry.register_document
class ReviewSourceDocument(Document):
    id = fields.IntegerField()
    name = fields.TextField()
    description = fields.TextField()

    class Index:
        name = 'sources'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = ReviewSource
