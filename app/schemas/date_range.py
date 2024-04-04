from datetime import date

from pydantic import BaseModel, model_serializer, model_validator


class DateRange(BaseModel):
    """
    DateRange is stored in a canonical form. Lower bound is inclusive, upper bound is exclusive.
    e.g. lower=1 upper=5 is [1,4)
    """

    lower: date
    upper: date

    @model_validator(mode='after')
    def check_date_range(self) -> 'DateRange':
        if self.lower >= self.upper:
            raise ValueError('lower bound must be before upper bound')
        return self


class DateRangeIn(DateRange):
    """
    Special DateRange type that converts the range to a format database will understand
    """
    @model_serializer
    def ser_model(self, *args, **kwargs) -> str:
        # Keep in mind:
        # interestingly, PostgreSQL will automatically convert inclusive upper bound to exclusive upper bound,
        # while adding one to the value (i.e. [1,5] becomes [1,6))
        # This happens for discrete ranges (with a well defined step) such as dates or numbers
        # https://www.postgresql.org/docs/current/rangetypes.html#RANGETYPES-DISCRETE

        # Since it's the canonical form, DateRange will also use inclusive lower and exclusive upper bounds
        return f'[{self.lower},{self.upper})'
