from typing import Optional
from pydantic import BaseModel, Field

from .date_range import DateRange
from app.schemas.date_range import DateRangeIn


# Shared properties
class ProjectBase(BaseModel):
    name: str = Field(min_length=1, max_length=32)
    description: Optional[str] = None


# Properties to receive on item creation
class ProjectCreate(ProjectBase):
    area_of_interest: dict
    date_range: DateRangeIn


# Properties to receive on item update
class ProjectUpdate(ProjectBase):
    # TODO fix the validation
    # TODO dont repeat type definition, find some way to make all fields optional
    name: Field(min_length=1, max_length=32, default=None)
    description: Optional[str] = None
    area_of_interest: Optional[dict] = None
    date_range: Optional[DateRangeIn] = None

    class Config:
        arbitrary_types_allowed=True


# Properties shared by models stored in DB
class ProjectInDBBase(ProjectBase):
    id: int
    area_of_interest: dict
    date_range: DateRange

    class Config:
        from_attributes = True


# Properties to return to client
class Project(ProjectInDBBase):
    area_of_interest: dict
    pass


# Properties stored in DB
class ProjectInDB(ProjectInDBBase):
    pass
