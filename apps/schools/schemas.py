from datetime import date

from ninja import ModelSchema

from .models import School


class SchoolSchema(ModelSchema):
    last_review: date = None
    aliases: list[str]
    rating: float

    class Config:
        model = School
        model_fields = '__all__'
