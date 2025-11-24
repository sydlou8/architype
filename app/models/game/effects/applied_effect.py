from sqlmodel import SQLModel, Field
from abc import ABC, abstractmethod
from typing import Any
from uuid import UUID, uuid4

from models.game.enums.stat_types import StatType

class AppliedEffect(SQLModel, ABC):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)

    effect_name: str | None = Field(default=None)
    description: str | None = Field(default=None)

    target: StatType | None = Field(default=None)
    is_unique_effect: bool = Field(default=False)           # Used for unique buffs/debuffs like stat debuffs from burn, poison, etc
    stat_magnifier: float | None = Field(default=0.0)            # This can be a float for percentage-based effects

    duration: int | None = Field(default=None)              # Duration in turns

    @abstractmethod
    def apply(self, duration: int = 1) -> None:
        '''Apply effect to entity'''
        pass