import decimal
from typing import Optional

from ninja import ModelSchema

from .models import Course


class CourseReadSchema(ModelSchema):
    rating: Optional[decimal.Decimal]
    school_name: str

    class Config:
        model = Course
        model_exclude = ['categories']
        model_fields_optional = '__all__'
