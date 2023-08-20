from ninja import ModelSchema

from .models import School


class SchoolSchema(ModelSchema):
    class Config:
        model = School
        model_fields = '__all__'
