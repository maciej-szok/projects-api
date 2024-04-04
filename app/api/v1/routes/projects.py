from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps



# TODO handle db exceptions
# TODO
router = APIRouter()


@router.post("/", response_model=schemas.Project, status_code=201)
def create_project(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.ProjectCreate,
) -> Any:
    """
    Create new project.
    """
    project = crud.project.create(db=db, obj_in=item_in)
    return project


@router.get("/", response_model=List[schemas.Project])
def read_projects(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve multiple projects.
    """
    # TODO validate skip and limit params
    items = crud.project.get_multi(db=db, skip=skip, limit=limit)
    return items


@router.get("/{project_id}", response_model=schemas.Project)
def read_project(
    *,
    db: Session = Depends(deps.get_db),
    project_id: int,
) -> Any:
    """
    Get project by ID.
    """
    project = crud.project.get(db=db, id=project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project


@router.put("/{project_id}", response_model=schemas.Project)
def update_project(
    *,
    db: Session = Depends(deps.get_db),
    project_id: int,
    project_in: schemas.ProjectUpdate,
) -> Any:
    """
    Update a project.
    """
    project = crud.project.get(db=db, id=project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    project = crud.project.update(db=db, db_obj=project, obj_in=project_in)
    return project


@router.delete("/{project_id}", response_model=schemas.ItemDeleted)
def delete_project(
    *,
    db: Session = Depends(deps.get_db),
    project_id: int,
) -> Any:
    """
    Delete a project.
    """
    project = crud.project.get(db=db, id=project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    project = crud.project.remove(db=db, id=project_id)
    return schemas.ItemDeleted(id=project.id)
