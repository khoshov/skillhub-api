from ninja import ModelSchema

from .models import Course


class CourseSchema(ModelSchema):
    class Config:
        model = Course
        model_exclude = ['categories']
