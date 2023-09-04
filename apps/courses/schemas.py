import decimal
from typing import Optional, Any

from ninja import ModelSchema

from .models import Course, Category


class CourseReadSchema(ModelSchema):
    rating: Optional[decimal.Decimal]
    school_name: str

    class Config:
        model = Course
        model_fields = '__all__'
        model_fields_optional = '__all__'


class CategoryChildReadSchema(ModelSchema):
    class Config:
        model = Category
        model_fields = '__all__'
        model_fields_optional = '__all__'


class CategoryReadSchema(ModelSchema):
    children: list[CategoryChildReadSchema]

    class Config:
        model = Category
        model_fields = '__all__'
        model_fields_optional = '__all__'
