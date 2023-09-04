from typing import Optional

from ninja import ModelSchema

from .models import Review, Criterion


class ReviewCreateSchema(ModelSchema):
    school_id: Optional[int] = None
    source_id: Optional[int] = None

    class Config:
        model = Review
        model_exclude = ['id', 'school', 'source']
        model_fields_optional = ['criteria']


class ReviewReadSchema(ModelSchema):
    school_id: Optional[int] = None
    source_id: Optional[int] = None

    class Config:
        model = Review
        model_exclude = ['school', 'source']
        model_fields_optional = '__all__'


class ReviewUpdateSchema(ModelSchema):
    school_id: Optional[int] = None
    source_id: Optional[int] = None

    class Config:
        model = Review
        model_exclude = ['id', 'school', 'source']
        model_fields_optional = '__all__'


class CriterionReadSchema(ModelSchema):
    class Config:
        model = Criterion
        model_fields = '__all__'
        model_fields_optional = '__all__'
