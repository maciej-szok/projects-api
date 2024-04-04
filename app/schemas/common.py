from pydantic import BaseModel


class ItemDeleted(BaseModel):
    id: int
