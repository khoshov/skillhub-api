from ninja import ModelSchema

from .models import Review, ReviewCriterion


class ReviewSchema(ModelSchema):
    class Config:
        model = Review
        model_fields = '__all__'
        model_fields_optional = ['id']


class ReviewCriterionSchema(ModelSchema):
    class Config:
        model = ReviewCriterion
        model_fields = '__all__'
