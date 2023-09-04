from typing import List

from django.db.models import Subquery, OuterRef, Avg, F
from django.db.models.functions import Round
from django.http import Http404
from ninja import Router

from reviews.models import Review
from .models import Course
from .schemas import CourseReadSchema

router = Router()


@router.get('/', response=List[CourseReadSchema])
async def list_courses(request, page: int = 1, page_size: int = 10):
    courses = Course.objects.annotate(
        rating=Subquery(
            Review.objects.filter(
                school_id=OuterRef('school_id')
            ).values('school__reviews').annotate(
                average_rating=Round(Avg('rating'), precision=1),
            ).values('average_rating')[:1]
        ),
        school_name=F('school__name')
    )[(page - 1) * page_size: page * page_size]
    return [course async for course in courses]


@router.get("/{slug}", response=CourseReadSchema)
async def get_course(request, slug: str):
    try:
        return await Course.objects.annotate(
            rating=Subquery(
                Review.objects.filter(
                    school_id=OuterRef('school_id')
                ).values('school__reviews').annotate(
                    average_rating=Round(Avg('rating'), precision=1),
                ).values('average_rating')[:1]
            ),
            school_name=F('school__name')
        ).aget(slug=slug)
    except Course.DoesNotExist:
        raise Http404(
            "No %s matches the given query." % Course._meta.object_name
        )

# @router.get('/', response=List[CourseSchema])
# async def list_categories(request, limit: int = 10, offset: int = 0):
#     courses = Category.objects.all()[offset: offset + limit]
#     return [course async for course in courses]
