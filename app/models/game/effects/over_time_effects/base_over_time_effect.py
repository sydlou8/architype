from abc import abstractmethod
from typing import Any
from sqlmodel import Field
from uuid import UUID, uuid4

from models.game.entities.base_entity import BaseEntity
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_over_time_effect import AppliedOverTimeEffect

class BaseOverTimeEffect(BaseEffect):
    tick_value: int | None = Field(default=None)  # Value per tick (e.g., damage per turn, healing per turn)

    # override abstract method signature in extending classes to include tick_value or movement_distance as needed
    @abstractmethod
    def generate_effects(self, entity: BaseEntity, tick_value: int = 0) -> list[AppliedOverTimeEffect]:
        """
        Generate the effects to be applied to the entity for over-time effects.
        These skills are applied then take effect at the beginning of each turn for the duration of the effect.
        
        Parameters:
            entity (BaseEntity): The entity to which the effect is applied.
            tick_value (int): The value associated with each tick of the effect 
                                   (e.g., damage per turn, healing per turn).
        """
        pass