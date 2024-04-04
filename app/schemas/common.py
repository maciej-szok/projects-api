from typing import Any

from pydantic import BaseModel


class ItemDeleted(BaseModel):
    id: int


class OptionalModel(BaseModel):
    @classmethod
    def __pydantic_init_subclass__(cls, **kwargs: Any) -> None:
        super().__pydantic_init_subclass__(**kwargs)

        for field in cls.model_fields.values():
            field.default = None

        cls.model_rebuild(force=True)
