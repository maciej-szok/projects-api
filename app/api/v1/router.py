from fastapi import APIRouter

from app.api.v1.routes import projects

api_router = APIRouter()
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
