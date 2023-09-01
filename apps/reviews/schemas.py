from ninja import ModelSchema

from .models import Review


class ReviewSchema(ModelSchema):
    class Config:
        model = Review
        model_fields = '__all__'
