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

    cooldown: int = Field(default=0)                    # Number of turns before the skill can be used again

    accuracy: float = Field(default=1)                  # Represents the chance of successfully hitting the target
    power: int = Field(default=0)                       # Represents the skill's power or effectiveness
    effect: BaseAbility | None = Field(default=None)    # Represents any special effect the skill may have

    is_multi_target: bool = Field(default=False)        # Whether the skill can target multiple entities
    is_multi_hit: bool = Field(default=False)           # Whether the skill hits multiple times

    @abstractmethod
    def use(self, user: BaseEntity, target: BaseEntity) -> None:
        """Use the skill on a target."""
        pass
    
    @abstractmethod
    def level_up(self) -> None:
        """Level up the skill, improving its attributes."""
        pass

    def calculate_base_damage(self, user: BaseEntity, target: BaseEntity, user_attack: StatType, target_defense: StatType) -> int:
        """Calculate the damage dealt by the skill based on attacker's attack stat and target's defense stat."""
        # Map StatType to the actual property names
        attack_value = 0
        defense_value = 0
        
        if user_attack == StatType.PHYSICAL_ATTACK:
            attack_value = user.current_physical_attack
        elif user_attack == StatType.MAGICAL_ATTACK:
            attack_value = user.current_magical_attack
            
        if target_defense == StatType.PHYSICAL_DEFENSE:
            defense_value = target.current_physical_defense
        elif target_defense == StatType.MAGICAL_DEFENSE:
            defense_value = target.current_magical_defense
        
        # Calculate damage using multiplicative mitigation formula:
        # damage = (skill_power% × attack) × (1 - defense_mitigation)
        # Defense mitigation caps at 75% to prevent invulnerability
        defense_mitigation = min(0.75, defense_value / 100)
        base_damage = (self.power / 100) * attack_value
        total_damage = int(base_damage * (1 - defense_mitigation))
        
        return total_damage