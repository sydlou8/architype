from abc import abstractmethod
from typing import Any
from sqlmodel import Field
from uuid import UUID, uuid4

from models.game.entities.base_entity import BaseEntity
from models.game.effects.base_effect import BaseEffect
from models.game.effects.applied_over_time_effect import AppliedOverTimeEffect

class BaseMovementEffect(BaseEffect):
    movement_distance: int | None = Field(default=None)  # Value per movement tick (e.g., distance moved per turn)
    move_chance: float | None = Field(default=None)  # Chance to move
   
    @abstractmethod
    def generate_effects(self, entity: BaseEntity, movement_distance: int = 0, move_chance: float = 0) -> list[AppliedOverTimeEffect]:
        """
        Generate the effects to be applied to the entity for over-time effects.
        These are applied immediately upon application.
        
        Parameters:
            entity (BaseEntity): The entity to which the effect is applied.
            movement_distance (int): The distance associated with each movement tick of the effect 
                                   (e.g., distance moved).
            move_chance (float): The chance to move associated with the effect.
        """
        pass