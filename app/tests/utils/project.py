from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.project import ProjectCreate
from app.tests.utils.utils import random_lower_string


def create_random_project(db: Session) -> models.Project:
    name = random_lower_string()
    description = random_lower_string()
    item_in = ProjectCreate(name=name, description=description, area_of_interest={})
    return crud.project.create(db=db, obj_in=item_in)
