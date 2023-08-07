from ninja import ModelSchema

from courses.models import Course


class CourseSchema(ModelSchema):
    class Config:
        model = Course
        model_fields = '__all__'
