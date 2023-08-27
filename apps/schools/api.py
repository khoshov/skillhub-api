from typing import List

from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Subquery, OuterRef, Q
from django.http import Http404
from ninja import Router

from reviews.models import Review
from .models import School
from .schemas import SchoolSchema

router = Router()


@router.get('/', response=List[SchoolSchema])
async def list_schools(request):
    schools = School.objects.annotate(
        last_review=Subquery(
            Review.objects.filter(
                school_id=OuterRef('id')
            ).order_by('-published').values('published')[:1]
        ),
        aliases=ArrayAgg('schoolalias__name', filter=Q(schoolalias__isnull=False)),
    )
    return [school async for school in schools]


@router.get("/{school_id}", response=SchoolSchema)
async def get_school(request, school_id: int):
    try:
        return await School.objects.aget(id=school_id)
    except School.DoesNotExist:
        raise Http404(
            "No %s matches the given query." % School._meta.object_name
        )
