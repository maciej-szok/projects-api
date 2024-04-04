from sqlalchemy import Column, Integer, UnicodeText
from sqlalchemy.types import Unicode
from sqlalchemy.dialects.postgresql import JSONB, DATERANGE

from app.db.base_class import Base


class Project(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Unicode(32))
    description = Column(UnicodeText, nullable=True)

    # https://docs.sqlalchemy.org/en/20/dialects/postgresql.html#sqlalchemy.dialects.postgresql.DATERANGE
    date_range = Column(DATERANGE)

    # https://docs.sqlalchemy.org/en/20/dialects/postgresql.html#sqlalchemy.dialects.postgresql.JSONB
    # generally faster than storing JSON in a TEXT column
    area_of_interest = Column(JSONB)
