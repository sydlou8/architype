from abc import abstractmethod
from sqlmodel import Field
from typing import Any
from uuid import UUID, uuid4

from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.stat_types import StatType

class AppliedOverTimeEffect(AppliedEffect):
    tick_value: int | None = Field(default=0)           # This will always be an integer for tick-based effects like damage over time or healing over time
    
    @abstractmethod
    def apply(self, duration: int = 0, tick_value: int = 0) -> None:
        '''Apply effect to entity'''
        pass