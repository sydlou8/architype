from sqlmodel import SQLModel, Field
from abc import ABC, abstractmethod
from typing import Any
from uuid import UUID, uuid4

from models.enums.stat_types import StatType

class AppliedEffect(SQLModel, ABC):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)

    effect_name: str | None = Field(default=None)
    description: str | None = Field(default=None)

    target: StatType | None = Field(default=None)
    is_unique_effect: bool = Field(default=False)           # Used for unique buffs/debuffs like stat debuffs from burn, poison, etc
    magnitude: float | None = Field(default=0.0)            # This can be a float for percentage-based effects
    tick_magnitude: int | None = Field(default=0)           # This will always be an integer for tick-based effects like damage over time or healing over time

    duration: int | None = Field(default=None)              # Duration in turns

    @abstractmethod
    def apply(self, duration: int = 0, tick_value: int = 0) -> None:
        '''Apply effect to entity'''
        pass