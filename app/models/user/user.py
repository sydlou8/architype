from sqlmodel import SqlModel, Field, Relationship
from pydantic import EmailStr
from typing import Any
from uuid import UUID, uuid4
from models.game.constants import TUTORIAL_PARTY

class User(SqlModel, table=True):
    """User model representing a user in the system. This is for Authentication and Account/System data"""
    id: UUID = Field(default_factory=uuid4, primary_key=True)

    username: str = Field(index=True, unique=True, nullable=False)
    email: EmailStr = Field(index=True, unique=True, nullable=False)
    hashed_password: str = Field(nullable=False)
