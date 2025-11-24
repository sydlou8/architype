from abc import ABC, abstractmethod
from typing import Any
from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

from models.game.entities.base_entity import BaseEntity
from models.game.abilities.base_ability import BaseAbility
from models.game.enums.skill_types import SkillType
from models.game.enums.stat_types import StatType

class BaseSkill(SQLModel, ABC):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)

    name: str | None = Field(default=None)
    skill_type: SkillType | None = Field(default=None)
    description: str | None = Field(default=None)
    level: int = Field(default=1)

    cooldown: int = Field(default=0)  # Number of turns before the skill can be used again

    accuracy: float = Field(default=1)  # Represents the chance of successfully hitting the target
    power: int = Field(default=0)  # Represents the skill's power or effectiveness
    effect: BaseAbility | None = Field(default=None)  # Represents any special effect the skill may have

    is_multi_target: bool = Field(default=False)  # Whether the skill can target multiple entities
    is_multi_hit: bool = Field(default=False)    # Whether the skill hits multiple times

    @abstractmethod
    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use the skill on a target."""
        pass
    
    @abstractmethod
    def level_up(self) -> None:
        """Level up the skill, improving its attributes."""
        pass

    def calculate_base_damage(self, user: BaseEntity, target: BaseEntity, user_attack: StatType, target_defense: StatType) -> int:
        """Calculate the damage dealt by the skill."""
        base_damage = 0
        base_damage += ((self.power/100) * user.stats_registry[user_attack])
        target_defense_value = target.stats_registry[target_defense]

        total_base_damage = base_damage - target_defense_value

        return total_base_damage