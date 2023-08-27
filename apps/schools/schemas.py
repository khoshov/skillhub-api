from datetime import date

from ninja import ModelSchema

from .models import School, SchoolAlias


class SchoolAliasSchema(ModelSchema):
    class Config:
        model = SchoolAlias
        model_fields = (
            'id',
            'name',
        )


class SchoolSchema(ModelSchema):
    last_review: date = None
    aliases: list[str]

    class Config:
        model = School
        model_fields = '__all__'
