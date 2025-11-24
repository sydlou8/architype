from abc import abstractmethod
from sqlmodel import Field
from typing import Any
from uuid import UUID, uuid4

from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.stat_types import StatType

class AppliedMovementEffect(AppliedEffect):
    movement_distance: int | None = Field(default=0)           # This will always be an integer for tick-based effects like damage over time or healing over time
    move_chance: float | None = Field(default=0.0)           # This can be a float for percentage-based effects like chance to move each turn
    
    @abstractmethod
    def apply(self, duration: int = 0, movement_distance: int = 0, move_chance: float = 0.0) -> None:
        '''Apply effect to entity'''
        pass