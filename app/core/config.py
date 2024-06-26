from typing import Any, Annotated

from pydantic import AnyHttpUrl, PostgresDsn, computed_field, BeforeValidator, AnyUrl
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Settings(BaseSettings):
    PROJECT_NAME: str = "Geo projects API"
    BACKEND_CORS_ORIGINS: Annotated[
        list[AnyUrl] | str, BeforeValidator(parse_cors)
    ] = []

    API_V1_PATH: str = "/api/v1"

    # default values that will work for local development
    SERVER_HOST: AnyHttpUrl = "http://0.0.0.0:3000"

    POSTGRES_SERVER: str = 'db'
    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD: str = 'changethis'
    POSTGRES_DB: str = 'projects'
    POSTGRES_PORT: int = 5432

    DEBUG: bool = False

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+psycopg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )

    MAX_PAGE_SIZE: int = 50

    model_config = SettingsConfigDict(case_sensitive=True)


settings = Settings()
