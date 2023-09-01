import asyncio
from typing import List

from django.http import Http404
from ninja import Router

from .models import Review, ReviewCriterion
from .schemas import ReviewSchema, ReviewCriterionSchema

router = Router()


@router.get('/', response=List[ReviewSchema])
async def list_reviews(request, limit: int = 10, offset: int = 0):
    reviews = Review.objects.prefetch_related(
        'criteria',
    ).order_by(
        '-published',
    )[offset: offset + limit]
    return [review async for review in reviews]


@router.get('/criteria', response=List[ReviewCriterionSchema])
async def list_criteria(request, limit: int = 10, offset: int = 0):
    criteria = ReviewCriterion.objects.all()[offset: offset + limit]
    return [criterion async for criterion in criteria]


@router.post("/")
async def create_review(request, payload: ReviewSchema):
    review = await Review.objects.acreate(**payload.dict())
    return {"id": review.id}


@router.put("/{review_id}")
async def update_review(request, review_id: int, payload: ReviewSchema):
    try:
        review = await Review.objects.aget(id=review_id)
        await asyncio.gather(*map(lambda k, v: setattr(review, k, v), payload.dict().items()))
        review.asave()
        return {"success": True}
    except Review.DoesNotExist:
        raise Http404(
            "No %s matches the given query." % Review._meta.object_name
        )


@router.get("/{review_id}", response=ReviewSchema)
async def get_review(request, review_id: int):
    try:
        return await Review.objects.aget(id=review_id)
    except Review.DoesNotExist:
        raise Http404(
            "No %s matches the given query." % Review._meta.object_name
        )
