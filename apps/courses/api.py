from typing import List

from django.http import Http404
from ninja import Router

from .models import Course
from .schemas import CourseSchema

router = Router()


@router.get('/', response=List[CourseSchema])
async def list_courses(request):
    return [blog async for blog in Course.objects.all()]


@router.get("/{course_id}", response=CourseSchema)
async def get_course(request, course_id: int):
    try:
        return await Course.objects.aget(id=course_id)
    except Course.DoesNotExist:
        raise Http404(
            "No %s matches the given query." % Course._meta.object_name
        )
