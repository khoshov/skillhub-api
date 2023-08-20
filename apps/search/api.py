from ninja import Router

from courses.documents import CourseDocument
from schools.documents import SchoolDocument

router = Router()


@router.get('/', response=list[dict])
def search(request, q: str):
    result = []
    query_params = {
        'query': q,
        'fuzziness': '3',
        'fields': ['name', 'description'],
    }

    for document in (CourseDocument, SchoolDocument):
        search_results = document.search().query('multi_match', **query_params)
        for item in search_results:
            result.append({
                'name': item.name,
                'description': item.description,
                'url': item.url
            })

    return result
