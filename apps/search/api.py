from django.conf import settings
from elasticsearch import AsyncElasticsearch
from ninja import Router

router = Router()

es = AsyncElasticsearch(settings.ELASTICSEARCH_DSL_URL)


@router.get('/')
async def search(request, q: str):
    resp = await es.search(
        body={'query': {'query_string': {'query': f'{q}~5'}}},
        size=10_000,
    )
    return resp['hits']
