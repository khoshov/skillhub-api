from typing import List

from django.http import Http404
from ninja import Router

from .models import School
from .schemas import SchoolSchema

router = Router()


@router.get('/', response=List[SchoolSchema])
async def list_schools(request):
    return [blog async for blog in School.objects.all()]


@router.get("/{school_id}", response=SchoolSchema)
async def get_school(request, school_id: int):
    try:
        return await School.objects.aget(id=school_id)
    except School.DoesNotExist:
        raise Http404(
            "No %s matches the given query." % School._meta.object_name
        )
