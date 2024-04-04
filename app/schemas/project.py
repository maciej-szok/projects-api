from typing import Optional, List

import pydantic
from pydantic import BaseModel, Field, ConfigDict
from sqlalchemy.dialects.postgresql import Range

from .common import OptionalModel
from .date_range import DateRange, DateRangeIn


# Shared properties
class ProjectBase(BaseModel):
    name: str = Field(min_length=1, max_length=32)
    # Max description length is an arbitrary large number, can be freely changed if needed
    description: Optional[str] = Field(max_length=2000, default=None)
    area_of_interest: dict


# Properties to receive on item creation
class ProjectCreate(ProjectBase):
    date_range: DateRangeIn


# Properties to receive on item update, inheriting from OptionalModel makes all fields optional
class ProjectUpdate(ProjectCreate, OptionalModel):
    pass


# Representation of the project in the database
class ProjectInDBBase(ProjectBase):
    id: int
    date_range: DateRange | Range

    model_config = ConfigDict(from_attributes=True)

    @pydantic.model_validator(mode="before")
    def check(self) -> "ProjectInDBBase":
        if isinstance(self.date_range, Range):
            self.date_range = DateRange(lower=self.date_range.lower, upper=self.date_range.upper)
        return self


# Properties to return to client
class Project(ProjectInDBBase):
    pass


class ProjectList(BaseModel):
    items: List[Project]
