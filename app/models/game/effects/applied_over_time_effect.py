from sqlmodel import Field
from typing import Any
from uuid import UUID, uuid4

from models.game.effects.applied_effect import AppliedEffect
from models.game.enums.stat_types import StatType

class AppliedOverTimeEffect(AppliedEffect):
    """
    A concrete over-time effect (DoT/HoT) that has been applied to an entity.
    Extends AppliedEffect with tick_value for damage/healing per turn.
    """
    tick_value: int | None = Field(default=0)           # This will always be an integer for tick-based effects like damage over time or healing over time
    
    def apply(self, duration: int = 0, tick_value: int = 0) -> None:
        """Apply effect to entity - concrete implementation."""
        # The actual tick damage/healing is handled by entity.apply_tick_damage()
        # This method exists for compatibility
        pass