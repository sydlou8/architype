# To Be used later after implementing database.
from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from datetime import datetime


class Battle(SQLModel, table=True):
    """Battle state -- tracks the state of a battle between two players."""

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    player_party_id: UUID #= Field(foreign_key="player.id")
    enemy_party_id: UUID #= Field(foreign_key="enemy.id")
    turn_count: int = 0
    is_active: bool = True
    winner: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    battle_log: str = "[]"  # A log of actions taken during the battle