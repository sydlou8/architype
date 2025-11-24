from sqlmodel import SqlModel, Field, Relationship
from typing import Any
from uuid import UUID, uuid4

from models.game.constants import TUTORIAL_PARTY

class Player(SqlModel, table=True):
    """Player model representing a player in the game."""
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="user.id", nullable=False)
    party: Party = Field(default_factory=lambda: TUTORIAL_PARTY)
    collection: list[CharacterCollection] = Relationship(back_populates="player")