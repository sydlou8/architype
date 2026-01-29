from abc import ABC, abstractmethod
from typing import Any, TYPE_CHECKING
from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

from models.game.entities.base_entity import BaseEntity

if TYPE_CHECKING:
    from models.game.effects.applied_effect import AppliedEffect

class BaseEffect(SQLModel, ABC):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)

    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    is_unique_effect: bool = Field(default=False)  # Whether the effect is unique (non-stackable)

    BUFF_MULTIPLIER: float = 2.0
    DEBUFF_MULTIPLIER: float = 0.5

    # override abstract method signature in extending classes to include tick_value or movement_distance as needed
    @abstractmethod
    def generate_effects(self, effect_duration: int = 0) -> list["AppliedEffect"]:
        """
        Generate the effects to be applied to the entity.
        Parameters:
            entity (BaseEntity): The entity to which the effect is applied.
            tick_value (int): The value associated with each tick of the effect if it is a tick-based effect (e.g., damage per turn, healing per turn).
        """
        pass