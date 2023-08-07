from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from .models import Course
from .schemas import CourseSchema

router = Router()


@router.get('/', response=List[CourseSchema])
def list_courses(request):
    qs = Course.objects.all()
    return qs


@router.get("/{course_id}", response=CourseSchema)
def get_course(request, course_id: int):
    courses = get_object_or_404(Course, id=course_id)
    return courses
