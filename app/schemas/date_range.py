from datetime import date
from pydantic import BaseModel, model_serializer


class DateRange(BaseModel):
    """
    Range is stored in a canonical form. Lower bound is inclusive, upper bound is exclusive.
    e.g. lower=1 upper=5 is [1,4)
    """

    # TODO validate that lower is before upper on creation and update
    lower: date
    upper: date


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
