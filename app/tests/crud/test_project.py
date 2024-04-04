from sqlalchemy.orm import Session

from app import crud
from app.schemas.date_range import DateRangeIn
from app.schemas.project import ProjectCreate, ProjectUpdate
from app.tests.utils.utils import random_lower_string


def test_create_project(db: Session) -> None:
    name = random_lower_string()
    description = random_lower_string()
    area_of_interest = {'field1': 'ok'}
    date_range = DateRangeIn(lower='2021-01-01', upper='2021-01-02')

    project_data = ProjectCreate(
        name=name,
        description=description,
        area_of_interest=area_of_interest,
        date_range=date_range,
    )

    item = crud.project.create(db=db, obj_in=project_data)
    assert item.name == name
    assert item.description == description
    assert area_of_interest == item.area_of_interest
    assert item.date_range.lower == date_range.lower
    assert item.date_range.upper == date_range.upper


def test_get_project(db: Session) -> None:
    name = random_lower_string()
    description = random_lower_string()
    area_of_interest = {'field1': 'ok'}
    date_range = DateRangeIn(lower='2021-01-01', upper='2021-01-02')

    project_data = ProjectCreate(
        name=name,
        description=description,
        area_of_interest=area_of_interest,
        date_range=date_range,
    )

    project = crud.project.create(db=db, obj_in=project_data)

    stored_project = crud.project.get(db=db, id=project.id)
    assert stored_project
    assert project.id == stored_project.id
    assert project.name == stored_project.name
    assert project.description == stored_project.description
    assert project.area_of_interest == stored_project.area_of_interest
    assert project.date_range == stored_project.date_range


def test_update_item(db: Session) -> None:
    name = random_lower_string()
    description = random_lower_string()
    area_of_interest = {'field1': 'ok'}
    date_range = DateRangeIn(lower='2021-01-01', upper='2021-01-02')

    project_data = ProjectCreate(
        name=name,
        description=description,
        area_of_interest=area_of_interest,
        date_range=date_range,
    )

    project = crud.project.create(db=db, obj_in=project_data)

    name2 = random_lower_string()
    update_data = ProjectUpdate(name=name2)
    updated_project = crud.project.update(db=db, db_obj=project, obj_in=update_data)

    assert updated_project.id == project.id
    assert updated_project.name == name2
    assert updated_project.description == project.description


def test_delete_item(db: Session) -> None:
    name = random_lower_string()
    description = random_lower_string()
    area_of_interest = {'field1': 'ok'}
    date_range = DateRangeIn(lower='2021-01-01', upper='2021-01-02')

    project_data = ProjectCreate(
        name=name,
        description=description,
        area_of_interest=area_of_interest,
        date_range=date_range,
    )

    project = crud.project.create(db=db, obj_in=project_data)
    project_removed = crud.project.remove(db=db, id=project.id)
    project_missing = crud.project.get(db=db, id=project.id)

    assert project_missing is None
    assert project_removed.id == project.id
    assert project_removed.name == project.name
    assert project_removed.description == project.description
