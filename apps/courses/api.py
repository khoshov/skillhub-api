from typing import List

from django.http import Http404
from ninja import Router

from .models import Course
from .schemas import CourseSchema

router = Router()


@router.get('/', response=List[CourseSchema])
async def list_courses(request, limit: int = 10, offset: int = 0):
    courses = Course.objects.all()[offset: offset + limit]
    return [course async for course in courses]


@router.get("/{course_id}", response=CourseSchema)
async def get_course(request, course_id: int):
    try:
        return await Course.objects.aget(id=course_id)
    except Course.DoesNotExist:
        raise Http404(
            "No %s matches the given query." % Course._meta.object_name
        )
