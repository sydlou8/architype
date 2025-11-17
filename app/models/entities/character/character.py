from abc import ABC, abstractmethod
from typing import Any
from sqlmodel import Field

from models.entities.base_entity import BaseEntity
from models.enums.character_classes import CharacterClasses
from models.enums.stat_types import StatType
from models.enums.skill_types import SkillType
from models.enums.effect_types import EffectType, effect_registry, register_effect

class Character(BaseEntity, ABC):
    role: str | None = None 
    current_experience: int = Field(default=0)
    max_experience: int = Field(default=100)
    # skills --> this will be a dictionary of skill names as enums and function of the skill
    # characters can only have 4 skills at a time
    skills: dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": str(self.id),
            "role": self.role,
            "level": self.level,
            "current_health": self.current_health,
            "max_health": self.max_health,
            "is_alive": self.is_alive,
            "current_experience": self.current_experience,
            "max_experience": self.max_experience,
            "skills": list(self.skills.keys()),
            "active_effects": list(self.active_effects.keys()),
        }

    def from_dict(self, data: dict[str, Any]) -> Character:
        self.id = data.get("id", self.id)
        self.level = data.get("level", self.level)
        self.current_health = data.get("current_health", self.current_health)
        self.max_health = data.get("max_health", self.max_health)
        self.is_alive = data.get("is_alive", self.is_alive)
        self.current_experience = data.get("current_experience", self.current_experience)
        self.max_experience = data.get("max_experience", self.max_experience)
        # skills would need to be handled separately
        return self
    
    def level_up(self) -> None:
        """Level up the character, increasing stats accordingly."""
        self.level += 1
        self.current_experience = 0
        self.max_experience = int(self.max_experience * 1.5)  # Increase required XP for next level
    
    def attack(self, skill: Skill, target: BaseEntity) -> None:
        damage = skill.use(self, target)
        target.take_damage(damage)

    def defend(self) -> None:
        applied_effect = AppliedEffect(
            effect_name=EffectType.DEFEND.value,
            description="Increases defense for one turn.",
            target=StatType.PHYSICAL_DEFENSE,
            is_unique_effect=True,
            magnitude=5.0,
            duration=1
        )
        self.add_effect(applied_effect)

    def take_damage(self, amount: int) -> None:
        pass  # Implementation of take damage logic
    
    def heal(self, amount: int ) -> None:
        pass  # Implementation of heal logic