import decimal
from typing import Optional

from ninja import ModelSchema

from .models import Course


class CourseSchema(ModelSchema):
    rating: Optional[decimal.Decimal]
    school_name: str

    class Config:
        model = Course
        model_exclude = ['categories']
