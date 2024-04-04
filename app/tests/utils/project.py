from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.date_range import DateRangeIn
from app.schemas.project import ProjectCreate
from app.tests.utils.utils import random_lower_string


def create_random_project(db: Session) -> models.Project:
    name = random_lower_string()
    description = random_lower_string()
    item_in = ProjectCreate(
        name=name,
        description=description,
        area_of_interest={'area': 'ok'},
        date_range=DateRangeIn(lower='2021-01-01', upper='2021-01-02')
    )
    return crud.project.create(db=db, obj_in=item_in)
