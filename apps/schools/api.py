from typing import List

from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Subquery, OuterRef, Q, Avg
from django.db.models.functions import Round
from django.http import Http404
from ninja import Router

from reviews.models import Review
from .models import School
from .schemas import SchoolReadSchema

router = Router()


@router.get('/', response=List[SchoolReadSchema])
async def list_schools(request, limit: int = 10, offset: int = 0):
    schools = School.objects.annotate(
        last_review=Subquery(
            Review.objects.filter(
                school_id=OuterRef('id')
            ).order_by('-published').values('published')[:1]
        ),
        rating=Subquery(
            Review.objects.filter(
                school_id=OuterRef('id')
            ).values('school__reviews').annotate(
                average_rating=Round(Avg('rating'), precision=1),
            ).values('average_rating')[:1]
        ),
        aliases=ArrayAgg('schoolalias__name', filter=Q(schoolalias__isnull=False)),
    )[offset: offset + limit]
    return [school async for school in schools]


@router.get("/{school_slug}", response=SchoolReadSchema)
async def get_school(request, school_slug: str):
    try:
        return await School.objects.aget(slug=school_slug)
    except School.DoesNotExist:
        raise Http404(
            "No %s matches the given query." % School._meta.object_name
        )
