from typing import List

from django.db.models import Subquery, OuterRef, Avg, F
from django.db.models.functions import Round
from django.http import Http404
from ninja import Router

from core.utils import get_descendants
from reviews.models import Review
from .models import Course, Category
from .schemas import CourseReadSchema, CategoryReadSchema

router = Router()


@router.get('/', response=List[CourseReadSchema])
async def list_courses(request, category: str = None, page: int = 1, page_size: int = 10):

    courses = Course.objects.annotate(
        rating=Subquery(
            Review.objects.filter(
                school_id=OuterRef('school_id')
            ).values('school__reviews').annotate(
                average_rating=Round(Avg('rating'), precision=1),
            ).values('average_rating')[:1]
        ),
        school_name=F('school__name')
    ).prefetch_related(
        'categories',
    )
    if category:
        categories = Category.objects.filter(slug=category)
        categories = await get_descendants(categories)
        courses = courses.filter(categories__in=categories)
    courses = courses.distinct()[(page - 1) * page_size: page * page_size]
    return [course async for course in courses]


@router.get('/categories', response=List[CategoryReadSchema])
def list_categories(request):
    categories = Category.objects.filter(
        parent__isnull=True,
    ).prefetch_related(
        'children',
    ).order_by(
        'sort_order',
    )
    return categories


@router.get('/categories/{category_slug}', response=List[CategoryReadSchema])
def get_category(request, category_slug):
    categories = Category.objects.prefetch_related(
        'children',
    ).get(slug=category_slug)
    return categories


@router.get("/{course_slug}", response=CourseReadSchema)
async def get_course(request, course_slug: str):
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
        ).prefetch_related(
            'categories',
        ).aget(slug=course_slug)
    except Course.DoesNotExist:
        raise Http404(
            "No %s matches the given query." % Course._meta.object_name
        )
