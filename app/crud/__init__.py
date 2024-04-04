from .base import CRUDBase
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate
# For a new basic set of CRUD operations you could just do
# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)

project = CRUDBase[Project, ProjectCreate, ProjectUpdate](Project)
