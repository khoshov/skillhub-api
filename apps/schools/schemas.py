import decimal
from datetime import date
from typing import Optional

from ninja import ModelSchema

from .models import School


class SchoolSchema(ModelSchema):
    aliases: list[str]
    last_review: Optional[date]
    rating: Optional[decimal.Decimal]

    class Config:
        model = School
        model_fields = '__all__'
