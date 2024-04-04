from typing import Any, List, Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.config import settings

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


# TODO: if more endpoint with pagination is needed,
#  consider creating a common system for the pagination or use a library
@router.get("/", response_model=List[schemas.Project])
def read_projects(
    db: Session = Depends(deps.get_db),
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=settings.MAX_PAGE_SIZE)] = 20,
) -> Any:
    """
    Retrieve multiple projects.
    """

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
