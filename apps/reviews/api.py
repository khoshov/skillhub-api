from typing import List

from django.http import Http404
from ninja import Router

from .models import Review
from .schemas import ReviewSchema

router = Router()


@router.get('/', response=List[ReviewSchema])
async def list_reviews(request, limit: int = 10, offset: int = 0):
    reviews = Review.objects.prefetch_related(
        'criteria',
    ).order_by(
        '-published',
    )[offset: offset + limit]
    return [review async for review in reviews]


@router.get("/{review_id}", response=ReviewSchema)
async def get_review(request, review_id: int):
    try:
        return await Review.objects.aget(id=review_id)
    except Review.DoesNotExist:
        raise Http404(
            "No %s matches the given query." % Review._meta.object_name
        )
