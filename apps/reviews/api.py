from typing import List

from aiostream import stream
from django.http import Http404
from ninja import Router

from .models import Review, Criterion
from .schemas import CriterionReadSchema, ReviewReadSchema, ReviewCreateSchema, ReviewUpdateSchema

router = Router()


@router.get('/', response=List[ReviewReadSchema])
async def list_reviews(request, limit: int = 10, offset: int = 0):
    reviews = Review.objects.prefetch_related(
        'criteria',
    ).order_by(
        '-published',
    )[offset: offset + limit]
    return [review async for review in reviews]


@router.get('/criteria', response=List[CriterionReadSchema])
async def list_criteria_variations(request, limit: int = 10, offset: int = 0):
    criteria = Criterion.objects.all()[offset: offset + limit]
    return [criterion async for criterion in criteria]


@router.post("/")
async def create_review(request, payload: ReviewCreateSchema):
    kwargs = payload.dict()
    criteria = kwargs.pop('criteria')
    review = await Review.objects.acreate(**kwargs)
    if criteria:
        await review.criteria.aset(criteria)
    return {"id": review.id}


@router.put("/{review_id}")
async def update_review(request, review_id: int, payload: ReviewUpdateSchema):
    try:
        kwargs = payload.dict()
        criteria = kwargs.pop('criteria')
        review = await Review.objects.aget(id=review_id)
        async for key, value in stream.iterate(kwargs.items()):
            if value:
                setattr(review, key, value)
        await review.asave()
        if criteria:
            await review.criteria.aset(criteria)
        return {"success": True}
    except Review.DoesNotExist:
        raise Http404(
            "No %s matches the given query." % Review._meta.object_name
        )


@router.get("/{review_id}", response=ReviewReadSchema)
async def get_review(request, review_id: int):
    try:
        return await Review.objects.prefetch_related(
            'criteria',
        ).aget(id=review_id)
    except Review.DoesNotExist:
        raise Http404(
            "No %s matches the given query." % Review._meta.object_name
        )
