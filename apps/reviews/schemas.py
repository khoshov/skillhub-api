from typing import Optional

from ninja import ModelSchema

from .models import Review, Criterion


class ReviewSchema(ModelSchema):
    school_id: Optional[int] = None
    source_id: Optional[int] = None

    class Config:
        model = Review
        model_exclude = ['school', 'source']
        model_fields_optional = '__all__'


class CriterionSchema(ModelSchema):
    class Config:
        model = Criterion
        model_fields = '__all__'
