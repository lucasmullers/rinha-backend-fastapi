from typing import Optional, List

from uuid import uuid4, UUID
from sqlmodel import SQLModel, Field, String, ARRAY, Column


class PessoasModel(SQLModel, table=True):
    __tablename__: str = "pessoas"
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True, index=True, nullable=False)
    apelido: str = Field(default_factory=str, max_length=32, unique=True, nullable=False)
    nome: str = Field(default_factory=str, max_length=100, nullable=False)
    nascimento: str = Field(default_factory=str, max_length=10, nullable=False, regex=r"\d{4}-\d{2}-\d{2}")
    stack: Optional[List[str]] = Field(default=None, sa_column=Column(ARRAY(String(32))), nullable=True)
