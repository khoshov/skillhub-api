from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import School


@registry.register_document
class SchoolDocument(Document):
    class Index:
        name = 'schools'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = School

        fields = [
            'name',
            'description',
        ]
